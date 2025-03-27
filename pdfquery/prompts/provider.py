import os.path


class PromptProvider:
    def __init__(self, fname : str = 'prompts.txt'):
        script_dirpath = os.path.dirname(__file__)
        fpath = os.path.join(script_dirpath, fname)
        if not os.path.isfile(fpath):
            raise FileNotFoundError(f'File {fpath} not found')
        with open(fpath, 'r') as f:
            file_content : str = f.read()
        segments = file_content.split(f'- ')

        self.segement_map : dict[str, str] = {}
        for s in segments:
            segment_name = s.split('\n')[0]
            content_lines = s.split('\n')[1:]
            segment_content = '\n'.join(content_lines)
            self.segement_map[segment_name] = segment_content

    def retrieve(self, name : str):
        """Retrieves a prompt from the specified prompt file by name"""
        return self.segement_map[name]



if __name__ == "__main__":
    prov = PromptProvider(fname='prompts.txt')
    prompt = prov.retrieve(name='refinement')
    print(f'done')

