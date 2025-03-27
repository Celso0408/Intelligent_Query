# PDFQuery

## Overview

This repository presents a framework for supporting LLMs in giving correct and consistent answers to queries on scientific papers
It is built out of the following modules which are described in more detail below:
- (1) PDFParser: Converts the pdf into a nicely formmated LLM readable form using libraries and custom methods; Currently supports markdown and Latex
- (2) Inference(+Language): Provides serval implementations for performing LLM inference; The language module allows for defining context in an implementation independent manner
- (3) Prompts: Prompts fed to the LLM when certain events are triggered
- (4) Data: Collection of papers accompanied with a set of questions and answers pertaining to the contents of the paper
- (5) Eval (+CoT): Implementation of Chain of thought structure that ensures verification of results; Serves as benchmarks to evaluate the performance of the framework based on queries+answers on real papers

Besides these modules the repository also contains a 'tests' module which ensures the integrity of the basic functions of modules. Each of these modules is explained in further detail below together with usage examples

## (1) Parser

The PDF parser is built on the "marker-pdf" library (https://github.com/VikParuchuri/marker) which converts
pdfs to markdown or latex code through pretrained models run through torch. Hence running this library in acceptable
timeframes likely requires a GPU powered system.

Additionally a custom table parser aligns the row of tables making them easier for LLMs (and humans) to read and work with.

Usage: Convert a pdf file to markdown. The output is a directory where a markdown.md file is accompanied by images representing the figures in the paper.
```python
from pdfquery.pdfparser import PdfParser
PdfParser.to_markdown(fpath='mypaper.pdf', target_dirpath='~/papers/mypaper') # Converts pdf to markdown
```

After preliminary testing of alternative python libraries marker-pdf has shown itself to be the best option in terms of recognizing formatting and equations.

## (2) Inference (+Language)

The purpose of the inference module is to provide a layer of abstraction between the implementation of the inference module and its usage.
Towards that end there is an abstract InferenceModule class which defines the Inference interface. Currently two inference modules are provided: GroqInf and OllamaInf, using Groq (https://groq.com/) and Ollama (https://ollama.com/) respectively.

Because these implementations may require conversation data in slighly different data structures, context is also defined in agnostic with respect to implementation.
The language module provides a "Context" class. This context class is consists of a list of "messages".

A message is made up of content (str) and possibly an image (PIL.Image), together with the information of who this message is attribute to i.e. the "role" (str) of the conversation participant.
Be aware however that as of 20.03.25 to the best of my knowledge only single image inference is supported. If inference with multiple image in context is attempted either an exception will be thrown or only the first/last image will be accounted for in the inference.
For example a "message" could be passed into the inference mechanism like so: "{'role' : 'Assistant', 'content' : 'Hello how can I help'}.

The process of performing inference on a desired context is simple by design and agnostic with respect to the implementation of the inference.
Contexts can also be added through the "+" operator to seamlessly extend the context throughout the course of the conversation.

Usage: Perform inference via Groq with an intial message requesting the agent to introduce itself
```python
from pdfquery.inference import GroqInf
from pdfquery.language import Context

inf_module = GroqInf(api_key=[your api key here])
initial_ctx = Context.singleton(content='Hello, please introduce yourself', role='user')
response = inf_module.get_response_text(context=initial_ctx, model='llama-3.3-70b-versatile')
```

Usage: Hold a conversation with the model on loop until exit condition is met
```python
from pdfquery.inference import GroqInf
from pdfquery.language import Context

inf = GroqInf(api_key=[your api key here])
ctx = Context.empty()
while True:
    user_msg = input("User: ")
    
    if user_msg == "exit":
        break
    
    ctx += Context.singleton(content=user_msg, role='user')
    response = inf.get_response_text(context = ctx)
    print(f'Assistant: {response}')
    ctx += Context.singleton(content=response, role='assistant') 
```

For more details on how Inference is performed refer to the GroqInf and OllamaInf implementations and the Groq and Ollama documentations (https://console.groq.com/docs/api-reference, https://github.com/ollama/ollama/blob/main/docs/api.md)

## (3) Prompts

The prompt module contains a text file with the prompts in plain text form and a provider module that provides a programmatic access to the prompts in the text file.
Currently there are only two prompts the text file.

One which asks the model to answer an initial query and a second prompt which instructs the model to review and if necessary
revise its initial answer. This second prompt also provides a checklist for the agent for possible error it should review its initial answer for.

Usage: Retrieve a prompt (str) from the prompts file
```python
from pdfquery.prompts.provider import PromptProvider

provider = PromptProvider()
query_prompt = provider.retrieve(name='query') # query_prompt = "Using the research paper provided to you, please answer the following question pertaining to the paper"
```

To see and edit prompts available through the PromptProvider look at the plain text file found in pdfquery/prompts/prompts.txt.

## (4) Data

The data folder includes 10 papers in both pdf and parsed from. This dataset was made to be as diverse as possible to best cover and represent all intended use cases of the pdfquery framework.

It includes two papers from each of these categories: Mathematics, Physics, Medicine, Foreign language papers and Miscellaneous. For each of these papers there's 10 questions paired with human written or human verified answers.
Each of these questions have definitive answers so that they can be checked against the correct answer programmatically. While the answers are either human written or human cross checked it isn't impossible that some errors remain so double
checking the validity of the question/answers is advised if the model consistently fails to answer correctly.

All of the above information is stored in the "data/" directory. The "curated/" directory contains the curated papapers in pdf, markdown and latex representation. In practice they are accessed in the code through a "ContextProvider" module.
This module retrieves a paper based on its paperID, which is just the name of the pdf in the "data/curated/pdf" directory, and then converts it to an LLM context. This context obejct is was introduced in module (2) Inference (+Language).

Usage: Generate context from paper with paperID 'phys1' and retrieve response to question about title of the paper
```python
from data.providers import ContextProvider
from pdfquery.inference import GroqInf
from pdfquery.language import Context

provider = ContextProvider()
groq_inf = GroqInf(api_key=[your api key here])
context = provider.get_context(pid='phys1')
context += Context.singleton(content=f'What is the title of this paper?')
response = groq_inf.get_response_text(context=context)
```

Currently the context is generated from the paper through feeding either a markdown or latex file to the model. If these files do not exist they are first generated from the pdf file through the PDFParser instead.

## (5) Eval (+CoT)

The eval module both includes the mechanism which evaluate the framework ont he curated dataset and contains the chain of Thought routine. At the moment the chain of thought is very simple:
- The model is initially challenged to answer the given query from the paper using the context that he is provided. This is using the prompt "query" as defined in prompts.txt
- He is then asked to review and if necessary revise his results. In doing so he is given a "refinement" prompt that details the steps that he is to take. These include
  - Reasoning about the question and defining the desired answer more clearly
  - Quoting relevant material from the text
  - Reasoning about the answer and the correctness of the intial answer from the quoted material
  - Standing by or revising the answer

This routine can be found in "eval/benchmarks/curated". Also in the "eval/benchmarks" are the files "numerical.py" and "spiqa.py".
The numerical.py executes a smaller scale benchmark where the agent is challenged to accurately extract numerical quantities from paper phys1.

The spiqa.py script evalutes the performance on the SPIQA dataset (https://github.com/google/spiqa). While the questions and paper in this dataset are generally
aligned with the purpose of pdfquery, rating their accuracy is difficult because the ground truth answers are sentences that can't be literally compared to answers given by the model.
It requires a mechanism with which to evalute whether the meaning of the ground truth and the model answers to the questions align which is costly and difficult. An attempt was made to do this
in the modle "eval/accuracy" but it does not perform very well.

Usage: Evalute Q&A performance on all papers stored stored in /data/curated
```python
import os
from pdfquery.inference import GroqInf
from eval.benchmarks.curated import CuratedEval
from data.providers import DocType

groq_inf = GroqInf(api_key=[your api key here])
paper_eval = CuratedEval(inf_module=groq_inf)
all_pids = os.listdir(paper_eval.file_provider.curated_pdf_dirpath)
paper_eval.evaluate(paper_ids=all_pids, doc_type=DocType.MARKDOWN)
```

The results of this evalution mechansim are documented in "eval/results". They all pertain the main evaluation benchmark from "eval/benchmarks/curated".