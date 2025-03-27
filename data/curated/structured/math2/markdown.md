### Algebraic Properties of Riemannian Manifolds

Youngjoo Chung a1 , Chi-Ok Hwang b2 and Hyun Seok Yang c3

a School of Electrical Engineering and Computer Science,

Gwangju Institute of Science and Technology, Gwangju 61005, Korea b Division of Liberal Arts and Sciences,

Gwangju Institute of Science and Technology, Gwangju 61005, Korea c Department of Physics and Photon Science,

Gwangju Institute of Science and Technology, Gwangju 61005, Korea

#### ABSTRACT

Algebraic properties are explored for the curvature tensors of Riemannian manifolds, using the irreducible decomposition of curvature tensors. Our method provides a powerful tool to analyze the irreducible basis as well as an algorithm to determine the linear dependence of arbitrary Riemann polynomials. We completely specify 13 independent basis elements for the quartic scalars and explicitly find 13 linear relations among 26 scalar invariants. Our method provides several completely new results, including some clues to identify 23 independent basis elements from 90 quintic scalars, that are difficult to find otherwise.

Keywords: Riemannian Manifolds, Curvature Invariants, Algebraic Identities of Riemann Tensors

August 17, 2023

<sup>1</sup> ychung@gist.ac.kr

<sup>2</sup> chwang@gist.ac.kr

<sup>3</sup>Corresponding Author:hsyang@gist.ac.kr

## 1 Introduction

The scalar invariants of the Riemann tensor Rabcd are important in general relativity since they allow a manifestly coordinate invariant characterization of certain geometrical properties of space-times. For example, they are important in studying curvature singularities [1, 2, 3], the classification of curvature tensors such as the Petrov type of the Weyl tensor Wabcd [4, 5], and the Segre type of the trace-free Ricci tensor Sab ≡ Rab− 1 4 δabR [6, 7, 8], and more generally in studying the equivalence problem, i.e., the question of whether two space-time metrics are equivalent [9, 10, 11]. See also [12, 13]. The scalar invariants are also important in understanding the structure of the diffeomorphism group and the effective action for quantum fields with gravitational interaction [14, 15, 16, 17].

The invariant characterization of a curved space must be in terms of scalars constructed from curvature tensors Rµνρσ and a metric tensor gµν . A simple argument implies (see §6.7 in [12]) that there are fourteen algebraically independent curvature invariants in four dimensions. Since the Riemann curvature tensor Rabcd has 20 independent components, the space of tensors Rabcd is 20-dimensional. But these twenty pieces of information are not independent because there are six degrees of freedom represented by the Lorentz transformation under which the metric is invariant. Hence there are 20 − 6 = 14 independent invariants (see §8.6 in [5]) that can be locally constructed by curvature tensors. However, the problem of obtaining a 'complete set' is not an easy problem since it requires to know all possible algebraic relations (known as *syzygies*) for the members of the set to any higher orders. This issue was one of the driving forces in the early development of computer algebra [18, 19].

The classification of the Riemann tensor in general relativity depends on properties of the algebraic invariants of the Weyl tensor and the Ricci tensor. For several decades, many attempts have been directed towards understanding these invariants and their relationships. In 1902 Haskins showed [20] that there were 14 independent differential invariants constructed from the metric tensor and the Riemann curvature tensor. Forty-five years later Narlikar and Karmarkar produced such a set of scalars [21, 22]. Sometime thereafter, G´eh´eniau and Debever also presented a set [23, 24, 25]. Various sets have been constructed by several authors [26, 27, 28, 29, 30] and have been claimed to be independent. However it was pointed out [31, 32, 33, 34] that the number of the sets proposed was deficient in some sense and none of these sets can be algebraically complete. Carminati and McLenaghan showed [31] that the 14 previously suggested invariants fail to describe solutions admitting a perfect fluid and came up with 16 independent invariants to cover all subspaces including the degenerate cases such as the Einstein-Maxwell theory and the perfect fluid. Later, Zahkary and McIntosh constructed the first complete set of algebraic invariants for all possible type of metrics [33]. This is an indication that the problem is not as straightforward as it may seem. The main difficulty is that the relationships between different invariants are not at all well understood.

The problem of linear dependences between the monomials (or polynomials) of the Riemann curvature tensor is not a simple question to answer. Because of the subtleties of tensor symmetry, terms may be linearly dependent in non-obvious ways. This problem was partially solved in [35] by applying some representation theory of the symmetric, general linear and orthogonal groups to the set formed from the Riemann tensor by covariant differentiation, multiplication and contraction. But the results of Ref. [35] are incomplete because

possible algebraic relations between the set of tensor polynomials were not addressed. Moreover only parity even polynomials have been included, so parity odd polynomials, i.e., pseudo-scalars or pseudo-tensors, are missing. In this paper we will develop a powerful tool to analyze the irreducible basis as well as an algorithm to determine the linear dependence of arbitrary Riemann polynomials using the irreducible decomposition of curvature tensors [36]. See also [37, 38, 39, 40].

A special feature of four-dimensional Riemannian manifolds is the fact that the Lie group Spin(4) splits into a product of two groups:

$Spin(4)=SU(2)_{+}\times SU(2)_{-}$.

The group Spin(4) is a double cover of the four-dimensional Euclidean Lorentz group SO(4), i.e., SO(4) = SU(2)+ × SU(2)−/Z2. It also leads to the splitting of the Lie algebra

$so(4)=su_{+}(2)\oplus su(2)_{-}$.

The splitting of the vector space g = so(4) is isomorphically related to the decomposition of the 2-forms on a four-manifold M. Using the Hodge ∗ operator acting on exterior 2-forms, one can split the 2-forms into self-dual and anti-self-dual 2-forms [41]

$\Omega^{2}\equiv\Lambda^{2}T^{*}M=\Omega^{2}_{+}\oplus\Omega^{2}_{-}$, (1.3)

where Ω 2 ± is the ±1 eigenspaces of the Hodge star operator ∗ : Ω2 → Ω 2 .

The splitting of the vector spaces, Eqs. (1.1) and (1.3), can be applied to the curvature form of any bundle with connection over an oriented four-manifold. The canonical splitting leads to the irreducible decomposition of Riemann curvature tensor R ∈ C∞(g ⊗ Ω 2 ) as [42, 43, 44]

$$R=R_{(++)}\oplus R_{(+-)}\oplus R_{(-+)}\oplus R_{(--)},\tag{1.4}$$

where the subscript (±, ±) refers to the splitting of the vector spaces g = so(4) = su+(2) ⊕ su(2)− and Ω 2 = Λ2T ∗M = Ω2 + ⊕ Ω 2 −. This splitting of the vector spaces occupies a central position of the Donaldson theory of four-manifolds and permeates four-dimensional geometry (see, for example, Chaps. 1.G in Ref. [43] and Secs. 1.1 and 2.1 in Ref. [41]). Essentially the same decomposition also appears in [26] (Eq. (10)) and [5] (Eq. (4.6.38)) using the spinor formalism and in [45, 46, 47] using complex self-dual bivectors. In particular, our approach corresponds to the real version of the latter, which clearly reveals an elegant structure for the Riemann polynomial under parity transformation.

This paper is organized as follows. In section 2, the index symmetries of the Riemann curvature tensor are reviewed which show how they reduce the number of independent index orders. In section 3, we review the results of [36]. We present the explicit form of the decomposition (1.4) for a general Riemannian manifold. The essentially same decomposition also appeared in the spinor approach for general relativity [5, 26], which has been used by most of the authors cited above. Since our method uses only vector indices rather than spinor indices [45, 46, 47], it is much simpler than the spinor method and is much more convenient for a practical calculation, even for developing computer algorithms. In section 4, we illustrate how the irreducible decomposition of curvature tensors (1.4) provides a powerful tool to analyze the irreducible basis as well as an algorithm to determine the linear dependence of arbitrary Riemann polynomials. After a brief application to the algebraic relation of some Riemann polynomials and the generalization of the Gauss-Bonnet relation to illustrate the power of our methodology, we completely specify 13 independent basis elements for the quartic scalars and explicitly find 13 linear relations among 26 scalar invariants. Our method also provides some clues to identification of 23 independent basis elements from 90 quintic scalars. We also clarify the algebraic properties of the second-rank cubic tensors, which was shown in [35] to have 16 basis elements. In section 5, we discuss future directions and suggest several generalizations. In particular, we address an issue of how to use our results in understanding the complete set of Riemann tensor invariants proposed in [31, 33].

All detailed results related to Chapter 4 are deferred to the appendices. Appendix A contains some useful identities of the 't Hooft symbols which are extensively used in our calculations. Appendix B is a warming-up calculation to show how effective our method is. We show *by hand* the vanishing of some quintic and quartic Riemann polynomials which were the examples presented in [48] to illustrate why the use of a computer is necessary since they are difficult to show by hand. Appendix C contains detailed results of the cubic scalars and second-rank tensors classified in [35]. We identify the independent basis elements of 8 cubic scalars by expanding them using the irreducible decomposition (1.4). We confirm that there are 6 independent cubic scalars and precisely reproduce the two algebraic relations found by Xu [49] and Harvey [50]. We extend the analysis to second-rank cubic tensors and get several new results. Appendix D contains our main results. We show in detail how the 26 quartic scalars in [35] can be expanded using the decomposition (1.4) and explicitly identify 14 basis elements. We find that these 14 basis elements are not completely independent and there is one more linear relation among them. This implies there must be 13 linear relations known as syzygies among the 26 quartic scalars. We found all of them. This completes the syzygies of Riemann curvature invariants in cubic and quartic orders.

### 2 Algebraic symmetry of the Riemann curvature tensor

A solution of gravitational field equations is given by the line element

$$ds^{2}=g_{\mu\nu}(x)dx^{\mu}dx^{\nu}=e^{a}\otimes e^{a}\tag{2.1}$$

with the symmetric, covariant metric tensor gµν or four basis covectors e a = e a µ (x)dxµ in a locally inertial frame. The basic objects of a metric are the Christoffel symbol and Riemann tensor which are defined as follows:

$$\Gamma^{\mu}_{\nu\lambda}=\frac{1}{2}g^{\mu\rho}\left(\frac{\partial g_{\rho\nu}}{\partial x^{\lambda}}+\frac{\partial g_{\rho\lambda}}{\partial x^{\nu}}-\frac{\partial g_{\nu\lambda}}{\partial x^{\rho}}\right)=\Gamma^{\mu}_{\lambda\nu},\tag{2.2}$$

$$R^{\mu}_{\ \nu\rho\sigma}=\frac{\partial\Gamma^{\mu}_{\nu\sigma}}{\partial x^{\rho}}-\frac{\partial\Gamma^{\mu}_{\nu\rho}}{\partial x^{\sigma}}+\Gamma^{\mu}_{\rho\lambda}\Gamma^{\lambda}_{\nu\sigma}-\Gamma^{\mu}_{\sigma\lambda}\Gamma^{\lambda}_{\nu\rho},\tag{2.3}$$

and Rµνρσ = gµλRλ νρσ. The Ricci tensor and Ricci scalar are defined by

$$R_{\mu\nu}=R^{\rho}{}_{\mu\rho\nu}=g^{\rho\sigma}R_{\rho\mu\sigma\nu},\qquad R=g^{\mu\nu}R_{\mu\nu}.\tag{2.4}$$

Throughout this paper, we will use the Riemann curvature tensor expressed in a locally inertial frame:

$$R_{abcd}=\epsilon^{\mu}_{a}\epsilon^{\nu}_{b}\epsilon^{\rho}_{c}\epsilon^{\sigma}_{d}R_{\mu\nu\rho\sigma}.\tag{2.5}$$

where ea = e µ a (x)∂µ are basis vectors defined by the conditions e µ a e b µ = δ b a and e µ a e a ν = δ µ ν .

From Eq. (2.3), one may read off the algebraic properties of the curvature tensor [12]:

(A) Antisymmetry

$$R_{abcd}=-R_{bacd}=-R_{abdc}=R_{bac}.\tag{2.6}$$

(B) The first Bianchi identity

$R_{abcd}+R_{acdb}+R_{adbc}=0$.

(C) Pair symmetry

$R_{abcd}=R_{cdab}$.

Indeed the last property (2.8) can be derived from (A) and (B). From these symmetries of the curvature tensor, it is easy to show [35] that of the 4! = 24 different possible orderings of the indices, only two are independent. A convenient choice of them is

$R_{abcd}$ and $R_{acbd}$.

### 3 Irreducible decomposition of curvature tensors

On an orientable Riemannian four-manifold, Eq. (1.3) shows that the 2-forms in Ω 2 (M) = Λ2T ∗M decompose into the space of self-dual and anti-self-dual 2-forms. Another important feature, which permeates four-dimensional geometry, is the fact that the Lorentz group Spin(4) splits into a product of two groups as expressed by Eq. (1.1). The group Spin(4) is a double cover of the four-dimensional Euclidean Lorentz group SO(4), i.e., SO(4) ∼= SU(2)+ × SU(2)−/Z2. The product structure (1.1) also leads to the splitting of the Lie algebra (1.2). The splitting of the vector space g = so(4) is defined by the chiral operator γ5 = −γ1γ2γ3γ4 in the Clifford algebra which obeys γ 2 5 = 1. Indeed, the splitting of vector spaces is induced by the existence of the projection operators [38]

$$P_{\pm}=\frac{1}{2}(1\pm*),\qquad P_{\pm}=\frac{1}{2}(1\pm\gamma_{5})\tag{3.1}$$

acting on the vector spaces Ω 2 and the so(4) generators Jab = 1 4 [γa, γb], respectively.

The explicit realization of the splitting (1.2) reads as

$$J_{ab}=J_{ab}^{+}\oplus J_{ab}^{-}\tag{3.2}$$

where J ± ab ≡ P±Jab and each part consists of three (2 × 2) anti-Hermitian traceless matrices. So they can be expanded in the basis of the Pauli matrices τ i (i = 1, 2, 3) as

$$J^{+}_{ab}=\frac{i}{2}\eta^{i}_{ab}\tau^{i}\in su(2)_{+},\qquad J^{-}_{ab}=\frac{i}{2}\bar{\eta}^{i}_{ab}\tau^{i}\in su(2)_{-},\tag{3.3}$$

where the expansion coefficients, the so-called 't Hooft symbols, are given by1

$$\eta^{i}_{ab}=-i{\rm Tr}\big{(}J^{+}_{ab}\tau^{i}\big{)},\qquad\bar{\eta}^{i}_{ab}=-i{\rm Tr}\big{(}J^{-}_{ab}\tau^{i}\big{)}.\tag{3.4}$$

An explicit representation of the 't Hooft symbols is shown up in Appendix A where we also list some useful identities of the 't Hooft symbols.

The decomposition (1.3) is that the six-dimensional vector space of two-forms canonically splits into the sum of three-dimensional vector spaces of self-dual and anti-self-dual two-forms. Canonical basis elements of self-dual and anti-self-dual two forms are given by

$$\zeta^{i}_{+}=\frac{1}{2}\eta^{i}_{ab}e^{a}\wedge e^{b}\in\Omega^{2}_{+},\qquad\zeta^{i}_{-}=\frac{1}{2}\bar{\eta}^{i}_{ab}e^{a}\wedge e^{b}\in\Omega^{2}_{-},\tag{3.5}$$

where the canonical basis elements satisfy the Hodge-duality equation

$$\begin{array}{l}\mbox{$\star$}\xi^{i}_{\pm}=\pm\xi^{i}_{\pm}.\end{array}\tag{3.6}$$

They also satisfy the intersection relation

$$\zeta^{i}_{\pm}\wedge\zeta^{j}_{\pm}=\pm2\delta^{ij}\sqrt{g}d^{4}x,\qquad\zeta^{i}_{\pm}\wedge\zeta^{j}_{\mp}=0.\tag{3.7}$$

The Riemann curvature tensor Rab = 1 2Rabµν dxµ ∧ dxν = 1 2Rabcde c ∧ e d ∈ C∞(g ⊗ Ω 2 ) is so(4)-valued 2-forms. Thus it is involved with two vector spaces g = so(4) and Ω 2 in (1.2) and (1.3). Let us apply the decompositions of the vector spaces g = so(4) and Ω 2 to Riemann curvature tensors. The first decomposition is that the Riemann tensor can be split into a pair of SU(2)+ and SU(2)− curvatures according to the Lie algebra splitting (3.2):

$$R_{ab}=F^{(+)i}\eta^{i}_{ab}+F^{(-)i}\bar{\eta}^{i}_{ab},\tag{3.8}$$

where SU(2)± field strengths are 2-forms on M defined by

$$F^{(\pm)i}=\frac{1}{2}F^{(\pm)i}_{cd}e^{c}\wedge e^{d}\tag{3.9}$$ $$=dA^{(\pm)i}-\varepsilon^{ijk}A^{(\pm)j}\wedge A^{(\pm)k}.$$

The second decomposition is that the SU(2)± field strengths in Eq. (3.8) can be decomposed as

$$F^{(+)i}=f^{ij}_{(++)}\zeta^{j}_{+}+f^{ij}_{(+-)}\zeta^{j}_{-},\qquad F^{(-)i}=f^{ij}_{(-+)}\zeta^{j}_{+}+f^{ij}_{(-)}\zeta^{j}_{-}.\tag{3.10}$$

Combining the two decompositions (3.8) and (3.10) leads to an irreducible decomposition of the general Riemann curvature tensor [36, 38]:

$$R_{abcd}=f^{ij}_{(++)}\eta^{i}_{ab}\eta^{j}_{cd}+f^{ij}_{(+-)}\eta^{i}_{ab}\bar{\eta}^{j}_{cd}+f^{ij}_{(-+)}\bar{\eta}^{i}_{ab}\eta^{j}_{cd}+f^{ij}_{(--)}\bar{\eta}^{i}_{ab}\bar{\eta}^{j}_{cd},\tag{3.11}$$

<sup>1</sup>The 't Hooft symbols, dubbed by physicists, were first introduced in [45, 46] as quantities (dubbed "tensor rotors") connecting a self-dual bivector to a vector in, so-called, "rotor space" and an anti-self-dual bivector to a complex conjugated rotor. See also [47]. The 't Hooft symbols have played an important role for instanton physics in Yang-Mills gauge theory [51].

which is the explicit form of the decomposition (1.4). Eq. (2.8) imposes the symmetry property

$$f^{ij}_{(++)}=f^{ji}_{(++)},\quad f^{ij}_{(--)}=f^{ji}_{(--)},\quad f^{ij}_{(+-)}=f^{ji}_{(-+)}.\tag{3.12}$$

The first Bianchi identity (2.7), being totally 16 conditions, imposes an additional constraint

$$f^{ij}_{(++)}\delta^{ij}=f^{ij}_{(--)}\delta^{ij}\tag{3.13}$$

that is equivalently written as

$\varepsilon^{abcd}R_{abcd}=0$.

The above results can be applied to the Ricci tensor Rab ≡ Racbc and the Ricci scalar R ≡ Raa to yield

$$R_{ab}=\left(f^{ij}_{(++)}\delta^{ij}+f^{ij}_{(--)}\delta^{ij}\right)\delta_{ab}+2f^{ij}_{(+-)}\eta^{i}_{ac}\bar{\eta}^{j}_{bc},$$ $$R=4\big{(}f^{ij}_{(++)}\delta^{ij}+f^{ij}_{(--)}\delta^{ij}\big{)}.\tag{3.15}$$

The "trace-free part" of the Riemann curvature tensor is called the Weyl tensor defined by

$$W_{abcd}=R_{abcd}-\frac{1}{2}(\delta_{ac}R_{bd}-\delta_{ad}R_{bc}-\delta_{bc}R_{ad}+\delta_{bd}R_{ac})+\frac{1}{6}(\delta_{ac}\delta_{bd}-\delta_{ad}\delta_{bc})R.\tag{3.16}$$

The Weyl tensor shares all the symmetry structures of the curvature tensor and all its traces with the metric are zero. Then the Weyl tensor can be decomposed as

$$W_{abcd}=f^{ij}_{(++)}\eta^{i}_{ab}\eta^{j}_{cd}+f^{ij}_{(--)}\bar{\eta}^{i}_{ab}\bar{\eta}^{j}_{cd}-\frac{1}{3}\Big{(}f^{ij}_{(++)}\delta^{ij}+f^{ij}_{(--)}\delta^{ij}\Big{)}(\delta_{ac}\delta_{bd}-\delta_{ad}\delta_{bc})\tag{3.17}$$ $$=\bar{f}^{ij}_{(++)}\eta^{i}_{ab}\eta^{j}_{cd}+\bar{f}^{ij}_{(--)}\bar{\eta}^{i}_{ab}\bar{\eta}^{j}_{cd},$$

where feij (++) ≡ f ij (++) − 1 3 δ ij f kl (++)δ kl and feij (−−) ≡ f ij (−−) − 1 3 δ ij f kl (−−) δ kl are symmetric, traceless 3 × 3 matrices. In the end the Riemann tensor is decomposed as

$$R_{abcd}=W_{abcd}+\frac{1}{12}R(\delta_{ac}\delta_{bd}-\delta_{ad}\delta_{bc})+f^{ij}_{(+-)}(\eta^{i}_{ab}\bar{\eta}^{j}_{cd}+\bar{\eta}^{j}_{ab}\eta^{i}_{cd})\tag{3.18}$$

where the last one corresponds to the traceless Ricci tensor Sab ≡ Rab − 1 4 δabR = 2f ij (+−) η i acη¯ j bc or, conversely, f ij (+−) = 1 8 Sabη i acη¯ j bc.

Using the decomposition (3.11) and (3.15), it is easy to calculate quadratic (pseudo-)scalars of curvature tensors

RabcdRabcd = 16 f ij (++)f ij (++) + 2f ij (+−) f ij (+−) + f ij (−−) f ij (−−) , RabRab = 4 f ij (++)δ ij + f ij (−−) δ ij2 + 16f ij (+−) f ij (+−) , R 2 = 16 f ij (++)δ ij + f ij (−−) δ ij2 , (3.19) ε abcdε ef ghRabefRcdgh = 64 f ij (++)f ij (++) − 2f ij (+−) f ij (+−) + f ij (−−) f ij (−−) , ε cdefRabcdRabef = 32 f ij (++)f ij (++) − f ij (−−) f ij (−−) .

One can immediately see that

$$R_{abcd}R_{abcd}-4R_{ab}R_{ab}+R^{2}=\frac{1}{4}\varepsilon^{abcd}\varepsilon^{effgh}R_{abef}R_{cdgh}.\tag{3.20}$$

This is the famous Gauss-Bonnet relation (see Appendix B in [52]) where the right-hand side is the well-known Euler density ρχ = 1 128π2 ε abcdε ef ghRabefRcdgh such that χ = R M ρχ √ gd4x = n ≥ 0. The last one in Eq. (3.19) corresponds to the Hirzebruch density ρτ = 1 96π2 ε cdefRabcdRabef in which the Hirzebruch signature is defined by τ = R M ρτ √gd4x = m ∈ Z [44, 53]. However, since the Hirzebruch density ρτ is a pseudo-scalar, ρτ cannot be written in a similar way as the Euler density ρχ.

Using the decomposition (3.17), it is easy to get

$$\begin{array}{r c l}{{W_{a c d e}W_{b c d e}}}&{{=}}&{{4\Big(f_{(++)}^{i j}f_{(++)}^{i j}+f_{(--)}^{i j}f_{(--)}^{i j}\Big)\delta_{a b}-\frac{1}{24}R^{2}\delta_{a b}}}\\ {{}}&{{}}&{{}}\\ {{}}&{{}}&{{=}}&{{4\Big(\tilde{f}_{(++)}^{i j}\tilde{f}_{(++)}^{i j}+\tilde{f}_{(--)}^{i j}\tilde{f}_{(--)}^{i j}\Big)\delta_{a b}.}}\end{array}$$

Using this result, one can get the important identity [35]

$$W_{cdea}W_{cdeb}=\frac{1}{4}\delta_{ab}W_{cdef}W_{cdef}.\tag{3.21}$$

Using the definition (3.16), it can be written as

$$R_{\alpha\dot{a}a}R_{\alpha\dot{b}b}=\frac{1}{4}\delta_{ab}R_{\alpha\dot{c}f}R_{\alpha\dot{f}}+2R_{\alpha\dot{b}b}R_{cd}+2R_{ac}R_{bc}-\delta_{ab}R_{cd}^{2}-R\left(R_{ab}-\frac{1}{4}\delta_{ab}R\right).\tag{3.22}$$

Under the parity transformation which flips the orientation of four-manifolds, the self-dual and anti-selfdual 't Hooft symbols exchange their role and it induces the interchange

$$f^{ij}_{(++)}\leftrightarrow f^{ij}_{(--)},\qquad f^{ij}_{(+-)}\leftrightarrow f^{ij}_{(-+)}=f^{ji}_{(+-)}.\tag{3.23}$$

Therefore the normal scalars and tensors which are invariant under the parity transformation must be symmetric for the interchange (3.23). The quadratic scalars in Eq. (3.19) exhibits this symmetry. But, pseudo-scalars and pseudo-tensors change the sign under the parity transformation and the Hirzebruch density shows this behavior.

For Einstein manifolds satisfying the equations, Rµν = λgµν (or Rab = λδab), with λ a cosmological constant, one can show [36, 40] that

$f^{ij}_{(+-)}=f^{ji}_{(-+)}=0$.

Therefore the curvature tensor for Einstein manifolds takes the simple form

$$R_{abcd}=f^{ij}_{(++)}\eta^{i}_{ab}\eta^{j}_{cd}+f^{ij}_{(--)}\bar{\eta}^{i}_{ab}\bar{\eta}^{j}_{cd}.\tag{3.25}$$

### 4 Algebraic relations of curvature tensors

We have already illustrated in Eq. (3.19) how efficient our method using the irreducible decomposition of curvature tensors (3.11) is to find algebraic relations among the curvature tensors such as (3.20). To further illustrate the power of our methodology, let us quote the following sentence in [48]:

It is difficult to show by hand that

$$R_{a_{1}a_{2}b_{1}b_{2}}R_{c_{1}c_{2}d_{1}d_{2}}R_{e_{1}a_{1}e_{2}c_{1}}R_{a_{2}b_{1}b_{2}e_{1}}R_{c_{2}d_{1}d_{2}e_{2}}=0.\tag{4.1}$$

This example does not require the use of the cyclic identity of the Riemann tensor. The next example is more difficult to prove:

2Ra1a2b1b2Rc1c2a1d1Rd2b1d1a2Rb2d2c1c2 + 4Ra1a2b1b2Rc1c2d1a1Rd2a2b1c1Rb2d1c2d2 (4.2) −Ra1a2b1b2Rc1c2d1a1Rd2a2c2c1Rb1b2d1d2 + 4Ra1a2b1b2Rd2d1b2c2Rc1c2d1a1Rd2a2b1c1 = 0.

In Appendix B, we have shown these equations *by hand* using the decomposition (3.25).

Now we will extend the calculation in Eq. (3.19) to general cases: Rank-r tensors (with r free indices) formed from the Riemann tensor by multiplication and contraction. Furthermore, we will generalize our calculations to general Riemannian manifolds after a brief warm-up with the Einstein manifold. Incidentally, our method can also be applied to a Lorentzian manifold although it is based on the decompositions (1.2) and (1.3) which are characteristic properties established in the Euclidean signature. The signature of the metric is irrelevant in studying the algebraic relationship of the curvature tensors of a Riemannian (or Lorentzian) manifold.2 Indeed we will see that our results are consistent with the previous results for Lorentzian manifolds.

#### 4.1 Quadratic order

The quadratic monomials of Riemann tensors are completely classified in [35]. The scalar monomials have three independent basis elements listed in Eq. (3.19). The independent basis elements are given by the product of f ij (±±) and f ij (±∓)

$$f^{ij}_{(++)}f^{ij}_{(++)}+f^{ij}_{(--)}f^{ij}_{(--)},\quad f^{ij}_{(+-)}f^{ij}_{(+-)},\quad(f^{ij}_{(++)}\delta^{ij}+f^{ij}_{(-)}\delta^{ij})^{2}=\frac{R^{2}}{16}.\tag{4.3}$$

Considering the parity symmetry (3.23), the expression clearly verifies why the quadratic scalars have only three independent basis elements. The Gauss-Bonnet relation in (3.19) is not a linear relation among the quadratic scalars but a simple consequence of the formula [52]

$$\varepsilon^{a b c d}\varepsilon^{e f g h}=\delta_{[e}^{a}\delta_{f}^{b}\delta_{g}^{c}\delta_{h]}^{d}$$

where [efgh] means anti-symmetrization over all four indices.

Although we will consider a general Riemannian manifold later, let us restrict, for the time being, our calculation to Einstein manifolds whose curvature tensors are given by (3.25). Let us point out why this restriction does not lose generality while making the calculation simple. The main reason is that both the Ricci tensor and Ricci scalar are non-zero in the case of Einstein manifolds so that the index structure of rank-r tensors is exactly the same as the general case. Furthermore, the Weyl tensor for an Einstein manifold takes the same

<sup>2</sup>There may be a subtlety for pseudo-tensors since the Wick rotation of the Levi-Civita tensor will introduce an extra imaginary factor i = √ −1. However, since the pseudo-tensor contains only an odd number of the Levi-Civita tensors, such a subtlety can be easily dealt with.

form as a general Riemannian manifold, as shown in (3.17).3 However, in the conventional approach of dealing directly with the Riemann curvature tensor, the restriction to the Einstein manifold is of little help.

Since determining the linear dependence of the monomials of curvature tensors at quadratic order is a trivial problem, we will instead generalize the Gauss-Bonnet relation to the case with four free indices. Let us illuminate how to find a generalized Gauss-Bonnet relation among homogeneous monomials of the Riemann tensor with explicit examples. For example, using the result (3.25), it is easy to get

$$R_{abef}R_{efcd}=4\big{(}f^{ik}_{(++)}f^{kj}_{(++)}\eta^{i}_{ab}\eta^{j}_{cd}+f^{ik}_{(--)}f^{kj}_{(--)}\eta^{i}_{ab}\eta^{j}_{cd}\big{)}.\tag{4.4}$$

Now we want to express the right-hand side of Eq. (4.4) in terms of the product of the Riemann tensors. We will use the relation

$$f^{ij}_{(+-)}=\frac{1}{16}R_{abcde}\eta^{i}_{ab}\eta^{j}_{cd},\qquad f^{ij}_{(--)}=\frac{1}{16}R_{abcde}\eta^{i}_{ab}\eta^{j}_{cd},\qquad f^{ij}_{(+-)}=\frac{1}{16}R_{abcde}\eta^{i}_{ab}\eta^{j}_{cd}=f^{ji}_{(-)}.\tag{4.5}$$

Plugging these expressions into Eq. (4.4) and using various identities of the 't Hooft symbols in Appendix A lead to the result

$$R_{abef}R_{efcd}=\frac{1}{12}(\varepsilon_{a_{1}a_{2}a}\varepsilon_{b_{1}b_{2}c_{1}c_{2}}R_{a_{1}a_{2}b_{1}b_{2}}R_{c_{1}c_{2}cd}+\varepsilon_{a_{1}a_{2}ab}\varepsilon_{c_{1}c_{2}cd}R_{a_{1}a_{2}b_{1}b_{2}}R_{b_{1}b_{2}c_{1}c_{2}}\tag{4.6}$$ $$+\varepsilon_{a_{1}a_{2}b_{1}b_{2}}\varepsilon_{c_{1}c_{2}cd}R_{ab_{1}a_{2}}R_{b_{1}b_{2}c_{1}c_{2}}).$$

This is a generalization of the Gauss-Bonnet relation (3.20) in the sense that contracting [ab] and [cd] leads to the relation. (Since we have assumed the Einstein manifold, the last two terms on the left-hand side of Eq. (3.20) cancel each other.) The cyclic symmetry (2.7) leads to the relation

$$R_{abef}R_{cedf}=R_{aebf}R_{cedf}=\frac{1}{2}R_{abef}R_{efcd}.\tag{4.7}$$

Similarly, we get

$$R_{abbf}R_{cdf}=\left(f^{ij}_{(+)}f^{ij}_{(+)}+f^{ij}_{(-)}f^{ij}_{(-)}\right)\delta_{ac}\delta_{bd}+2f^{ij}_{(+)}f^{kl}_{(-)}(\eta^{i}_{ac}\bar{\eta}^{k}_{ac})\left(\eta^{i}_{bj}\bar{\eta}^{l}_{dj}\right)\tag{4.8}$$ $$+e^{ikm}\varepsilon^{ijn}f^{ij}_{(+)}f^{kl}_{(+)}\eta^{mn}_{ac}\eta^{n}_{bd}+e^{ikm}\varepsilon^{ijn}f^{ij}_{(-)}f^{kl}_{(-)}\bar{\eta}^{mn}_{ac}\bar{\eta}^{n}_{bd}.$$

Using the identity ε ikmε jln = δ i [j δ k l δ m n] where [jln] means anti-symmetrization over all three indices, and the relations,

$$f^{ij}_{(+)}\eta^{i}_{ab}\eta^{j}_{cd}=\frac{1}{2}\Big{(}R_{abcd}+\frac{1}{2}\varepsilon_{abef}R_{efcd}\Big{)},$$ $$f^{ij}_{(-)}\bar{\eta}^{i}_{ab}\bar{\eta}^{j}_{cd}=\frac{1}{2}\Big{(}R_{abcd}-\frac{1}{2}\varepsilon_{abef}R_{efcd}\Big{)},\tag{4.9}$$

we obtain, after a little algebra, the result

$$R_{abbf}R_{cdf}=R_{acf}R_{cfbd}+\frac{1}{16}R^{2}\big{(}\delta_{ab}\delta_{cd}-\delta_{ad}\delta_{bc}\big{)}-\frac{1}{2}RR_{abcd}\tag{4.10}$$ $$-\frac{1}{8}R_{a_{1}a_{2}b_{1}}R_{a_{1}a_{2}b_{2}}\big{(}\delta_{ab}\delta_{cd}-\delta_{ad}\delta_{bc}-\delta_{ac}\delta_{bd}\big{)}$$ $$-\frac{1}{4}\varepsilon_{aaa_{1}a_{2}}\varepsilon_{cab_{1}b_{2}}R_{a_{1}a_{2}b_{2}}fR_{b_{1}b_{2}df}+\frac{1}{16}\varepsilon_{abcd}\varepsilon_{a_{1}a_{2}b_{1}b_{2}}R_{c_{1}c_{2}a_{1}a_{2}}R_{c_{1}c_{2}b_{2}b_{2}}.$$

<sup>3</sup>Therefore, the result for an Einstein manifold can easily be converted to the result for the Weyl tensor of a general Riemannian manifold using the relation (3.17) which can be written as Wabcd = R E abcd − 1 12R(δacδbd −δadδbc) where R E abcd is the Riemann tensor given by (3.25). See, for example, Eqs. (3.21) and (3.22).

Using the cyclic symmetry (2.7) leads to the relation

$$R_{a e b f}R_{c f d e}=R_{a e b f}R_{c e d f}-\frac{1}{2}R_{a b e f}R_{e f c d}.\tag{4.11}$$

But, directly plugging (4.5) into Eq. (4.8) leads to a different expression of the same result

RaebfRcedf = 1 12 εaea1a2 εbfb1b2RcedfRa1a2b1b2 + εcea1a2 εdfb1b2RaebfRa1a2b1b2 + 1 48 εaea1a2 εbfb1b2 εcec1c2 εdfd1d2Ra1a2b1b2Rc1c2d1d2 (4.12) = − 1 4 δacRbea1a2Rdea1a2 + δbdRaea1a2Rcea1a2 − 1 2 δacδbdRa1a2b1b2Ra1a2b1b2 + 1 8 εaea1a2 εbfb1b2RcedfRa1a2b1b2 + εcea1a2 εdfb1b2RaebfRa1a2b1b2 . (4.13)

By contracting c and d in Eq. (4.10) and b and d in Eqs. (4.12) and (4.13), we get

$$R_{a\sigma\epsilon f}R_{b\epsilon\epsilon f}=\frac{1}{4}\delta_{ab}R_{a_{1}a_{2}b_{1}b_{2}}R_{a_{1}a_{2}b_{1}b_{2}}\tag{4.14}$$ $$=\frac{1}{12}(\varepsilon_{ca_{1}a_{2}}\varepsilon_{b_{1}b_{2}c_{1}c_{2}}R_{bc_{1}c_{2}}R_{a_{1}a_{2}b_{1}b_{2}}+\varepsilon_{ba_{1}a_{2}}\varepsilon_{b_{1}b_{2}c_{1}c_{2}}R_{ac_{1}c_{2}}R_{a_{1}a_{2}b_{1}b_{2}}$$ $$+\varepsilon_{ac_{1}a_{2}}\varepsilon_{b_{2}b_{1}b_{2}}R_{a_{1}a_{2}c_{2}}R_{b_{1}b_{2}c_{1}c_{2}}),$$

and

$$\delta_{ab}R_{a_{1}a_{2}b_{1}b_{2}}R_{a_{1}a_{2}b_{1}b_{2}}=\frac{1}{2}\big{(}\varepsilon_{aa_{1}a_{2}}\varepsilon_{b_{1}b_{2}b_{1}c_{1}c_{2}}R_{bc_{1}c_{2}}R_{a_{1}a_{2}b_{1}b_{2}}+\varepsilon_{bca_{1}a_{2}}\varepsilon_{b_{1}b_{2}c_{1}c_{2}}R_{ac_{1}c_{2}}R_{a_{1}a_{2}b_{1}b_{2}}\big{)}\tag{4.15}$$ $$=\varepsilon_{aa_{1}a_{2}}\varepsilon_{bab_{1}b_{2}}R_{a_{1}a_{2}c_{1}c_{2}}R_{b_{1}b_{2}c_{1}c_{2}}.$$

We can also find algebraic relations for pseudo-tensors. There are four types at quadratic order:

εa1a2b1b2Raba1a2Rcdb1b2 = 1 3 εaba1a2Rcdb1b2 + εcdb1b2Raba1a2 Ra1a2b1b2 + 1 12 εaba1a2 εcdc1c2 εb1b2d1d2Ra1a2b1b2Rc1c2d1d2 , εa1a2b1b2Raba1a2Rcb1db2 = 1 2 εa1a2b1b2Raba1a2Rcdb1b2 , εa1a2b1b2Raa1ba2Rcb1db2 = 1 4 εa1a2b1b2Raba1a2Rcdb1b2 , (4.16) εaa1a2a3Rba1a3a4Rcda2a4 = − 1 8 εcdefRRabef + 1 4 εa1a2b1b2Raba1a2Rcdb1b2 , εaa1a2a3Rba1a3a4Ra2ca4d = 1 32 εa1a2b1b2Rc1c2a1a2Rc1c2b1b2 (δacδbd − δabδcd + δbcδad) + 1 4 εa1a2b1b2Raca1a2Rbdb1b2 − 1 2 εbdefRRefac + 1 16 εabcd Ra1a2b1b2Ra1a2b1b2 − 2Ra1a2Ra1a2 ,

$$\varepsilon_{aba_{1}a_{2}}R_{cdb_{1}b_{2}}R_{a_{1}a_{2}b_{1}b_{2}}=\varepsilon_{a_{1}a_{2}b_{1}b_{2}}R_{aba_{1}a_{2}}R_{cdb_{1}b_{2}},$$ $$\varepsilon_{aba_{1}a_{2}}R_{ca_{1}b_{1}b_{2}}R_{db_{1}a_{2}b_{2}}=\frac{1}{2}\varepsilon_{aba_{1}a_{2}}R_{ca_{1}b_{1}b_{2}}R_{da_{2}b_{1}b_{2}},\tag{4.17}$$ $$\varepsilon_{abca_{1}}R_{a_{1}a_{2}a_{3}a_{4}}R_{da_{3}a_{4}a_{2}}=-\frac{1}{2}\varepsilon_{ab\alpha_{1}}R_{a_{1}a_{2}a_{3}a_{4}}R_{da_{2}a_{3}a_{4}}.$$

Contracting (a, b) and (c, d) all leads to the Hirzebruch density in (3.19) except the last one which identically vanishes.

#### 4.2 Cubic order

We also want to generalize the calculation to higher orders. At higher orders, many terms are involved. So, at the cubic order, we will consider scalars and tensors with 2 free indices, for simplicity. It is known [35] that, at the cubic order, there are 8 types of scalar monomials made of Riemann curvature tensors:

- One curvature-scalar term: R3 ,
- Two Ricci terms: RRabRab, RabRbcRca,
- Five Riemann terms: RacRbdRabcd, RRabcdRabcd, RabRacdeRbcde, RabcdRcdefRefab, RacbdRcedfReafb.

Among the five Riemann terms, RabRacdeRbcde = 1 4RRabcdRabcd and RacRbdRabcd = 1 16R3 for Einstein manifolds which satisfy Rab = 1 4Rδab. But there is another relation, which can be found by expanding the last two terms:

RabcdRcdefRefab = 64 f i1i2 (++)f i1j1 (++)f i2j1 (++) + f i1i2 (−−) f i1j1 (−−) f i2j1 (−−) , RacbdRcedfRebfa = 1 16 R 3 − 6R f i1i2 (++)f i1i2 (++) + f i1i2 (−−) f i1i2 (−−) + 16 f i1i2 (++)f i1j1 (++)f i2j1 (++) + f i1i2 (−−) f i1j1 (−−) f i2j1 (−−) .

Therefore, we get the relation

$$R_{abcd}R_{cdef}R_{abef}-4R_{abcd}R_{cdef}R_{cbfa}=-\frac{1}{4}R^{3}+\frac{3}{2}RR_{abcd}R_{abcd},\tag{4.18}$$

which can be written as the relation among the Riemann terms

$$R_{abcd}R_{cbf}R_{efab}-4R_{acbd}R_{cbf}a+4R_{ac}R_{bd}R_{abcd}-6R_{ab}R_{acdc}R_{bcdc}=0.\tag{4.19}$$

Thus only three of the five Riemann terms can remain independent [35]. Using the relation

$$R^{3}-12RR_{ab}R_{ab}+16R_{ab}R_{bc}R_{ca}+3RR_{abcd}R_{abcd}+24R_{ac}R_{bd}R_{abcd}-24R_{ab}R_{acdc}R_{bcdc}$$ $$=\frac{1}{2}R^{3}-3RR_{abcd}R_{abcd},\tag{4.20}$$

we obtain the famous identity in the cubic order (see Eq. (3.5) in [35]):

$$R_{[ab}{}^{ab}R_{cd}{}^{cd}R_{ef]}{}^{ef}=\frac{1}{90}\left(R^{3}-12RR_{ab}R_{ab}+16R_{ab}R_{ac}R_{bc}+3RR_{abcd}R_{abcd}+24R_{ac}R_{bd}R_{abcd}\right.\tag{4.21}$$ $$\left.-24R_{ab}R_{acdc}R_{bcdc}+2R_{abcd}R_{cdf}R_{efab}-8R_{acbd}R_{ecf}R_{abfa}\right)=0,$$

where [· · · ] means anti-symmetrization over all six subscripts.

D. Xu had derived other identities related to the cubic scalars [49]:

$$R_{ab}R_{acdc}R_{bcdc}=\frac{1}{4}R^{3}-2RR_{ab}R_{ab}+2R_{ab}R_{bc}R_{ca}+2R_{ac}R_{bd}R_{abcd}+\frac{1}{4}RR_{abcd}R_{abcd},\tag{4.22}$$ $$R_{abcd}R_{caf}R_{cafb}=-\frac{5}{8}R^{3}+\frac{9}{2}RR_{ab}R_{ab}-4R_{ab}R_{bc}R_{ca}-3R_{ac}R_{bd}R_{abcd}-\frac{3}{8}RR_{abcd}R_{abcd}$$ $$+\frac{1}{2}R_{abcd}R_{cbf}R_{efab}.\tag{4.23}$$

The first identity (4.22) can be derived from Eq. (3.22) by contracting Rab on both sides [35]. A. Harvey pointed out [50] that the identities (4.22) and (4.23) can be derived from the fact [35] that an (n + 1) index object anti-symmetrized on an n-dimensional manifold vanishes identically. Indeed, Eqs. (4.22) and (4.23) can be derived from the identities, respectively,

$$\delta^{p}_{[a}\delta^{q}_{b}\delta^{r}_{c}\delta^{s}_{d}\delta^{t}_{e]}R_{abpq}R_{cdrs}R_{et}=0,\qquad\delta^{p}_{[a}\delta^{q}_{b}\delta^{r}_{c}\delta^{s}_{d}\delta^{t}_{e]}R_{abpq}R_{cdrs}R_{efu}=0.\tag{4.24}$$

His argument implies that these two identities are the only linear relations existing in the cubic terms. In fact, the identity (4.21) can be derived by combining the identities (4.22) and (4.23) and using the identity

$$R_{a c b d}R_{c e d f}R_{e b f a}=R_{a c b d}R_{c e d f}R_{e a f b}-\frac{1}{4}R_{a b c d}R_{c d e f}R_{e f a b}.$$

In Appendix C, we prove that the identities (4.22) and (4.23) are the only linear relations existent in the cubic terms for a general Riemannian manifold. This means that the cubic scalars have six independent basis elements.4

The second-rank tensors at the cubic order (i.e., with 2 free indices) are listed in Table 1 which reproduces the table in Appendix C, denoted by R2 6,3 , in [35]. As in the scalar terms, each term can be expanded using Eq. (3.11) and the result has more complicated expansions compared to the scalar case. This is because some terms vanishing in the case of a scalar are included. For example, we have the expansion

RRacRbc = R R2 16 δab − Rfij (+−) η i η¯ j ab + 4f ij (+−) f ij (+−) δab + 4ε i1i2i3ε j1j2j3f i1j1 (+−) f i2j2 (+−) η i3 η¯ j3 ab. (4.25)

The expansion of second-rank cubic monomials using Eq. (3.11) exhibits some patterns. The second-rank cubic monomials in Table 1 are symmetric with respect to (a ↔ b) except in G and J. It turns out that terms that would appear in the scalar case again appear with the factor 1 4 δab, and novel terms that do not appear in the scalar case (or should disappear in the scalar case) appear with the factor (η iη¯ j )ab. Indeed, δab and (η iη¯ j )ab are the only symmetric tensors constructed from the product of 't Hooft symbols. The latter is trace-free due to Eq. (A.5). The details are listed in Appendix C.

4Our approach can also be applied to pseudo-tensors. For example, we get

$e^{b_{1}b_{2}b_{3}b_{4}}R_{aa_{1}b_{1}b_{2}}R_{ba_{3}a_{1}a_{2}}R_{a_{2}a_{3}b_{3}b_{4}}=-16\left(f^{i_{1}i_{3}}_{(+\frac{1}{2})}f^{i_{1}i_{2}}_{(+\frac{1}{2})}f^{i_{3}i_{2}}_{(+\frac{1}{2})}-f^{i_{1}i_{3}}_{(-\frac{1}{2})}f^{i_{1}i_{2}}_{(-\frac{1}{2})}\right)\delta_{ab}$.

However, pseudo-tensors also have as many basis elements as normal tensors, and systematically classifying them as in Ref. [35] is a new problem. We leave this issue as a problem addressed in the future. But, it would be possible to know how to generate a pseudo-scalar basis that is parity odd, as we will discuss later.

| A:  |||| R2Rab       |||| I:  |||| RabRcdefRcdef    |
| --- |||| ---         |||| --- |||| ---              |
| B:  |||| RRacRbc     |||| J:  |||| RacRbedfRcedf    |
| C:  |||| RabRcdRcd   |||| K:  |||| RaecdRbfcdRef    |
| D:  |||| RacRbdRcd   |||| L:  |||| RacbdRcedfRef    |
| E:  |||| RRacbdRcd   |||| M:  |||| RacdeRbcdfRef    |
| F:  |||| RacbdRceRde |||| N:  |||| RagcdRbgefRcdef  |
| G:  |||| RacRbecdRde |||| O:  |||| RaecgRbfdgRcdef  |
| H:  |||| RRaecdRbecd |||| P:  |||| RaebgRcdefRcdf g |



Table 1: The 16 second-rank tensors at cubic order

#### 4.3 Quartic order

The 26 quartic scalars are listed in Table 2 which reproduces the last table in Appendix B, denoted by R0 8,4 , in [35]. A. Harvey found six linear relations [50] among the 26 monomials in Table 2 using the fact [35] that

| A:  || R4               || N: RabRcdRaecfRbedf       |
| --- || ---              || ---                       |
| B:  || R2RabRab         || O: RRabcdRcdefRefab       |
| C:  || RRabRbcRca       || P: RRacbdRaebfRcedf       |
| D:  ||   RabRab2       || Q: RabRacbdRef gcRef gd   |
| E:  || RabRbcRcdRda     || R: RabRcdefRagefRbgcd     |
| F:  || RRabRcdRacbd     || S: RabRcedfRegfaRgcbd     |
| G:  || RabRceRedRacbd   || T:   RabcdRabcd2         |
| H:  || R2RabcdRabcd     || U: RabcdRabceRf ghdRf ghe |
| I:  || RRabRacdeRbcde   || V: RabcdRcdefRef ghRghab  |
| J:  || RabRabRcdefRcdef || W: RabcdRabefRceghRdf gh  |
| K:  || RabRbcRdefaRdefc || X: RabcdRefabRgcheRgdhf   |
| L:  || RabRcdRacefRbdef || Y: RacbdRcedfRegfhRgahb   |
| M:  || RabRcdRaebfRcedf || Z: RacbdReafbRgehcRf gdh  |


Table 2: The 26 quartic scalars

an (n + 1) index object anti-symmetrized on an n-dimensional manifold vanishes identically.5 Therefore he reduced the number of independent scalars shown in Table 2 from 26 to 20. He pointed out that his method does

<sup>5</sup>We found several errors in Ref. [50]. These are corrected in Appendix D. Rectification of such errors played a crucial role in finding the correct independent basis.

not rule out the possible existence of other identities further reducing this number. We prove that the quartic scalars in Table 2 only have the 13 independent basis elements. This result implies that there must be 13 linear relations among the quartic monomials in Table 2. We explicitly find such linear relations. Therefore we found that there are seven more linear relations in addition to the 6 relations found by Harvey [50]. The details defer to Appendix D. Our method pins down that no more linear relation exists.

#### 4.4 Independent basis elements of quintic scalars

Our method using the decomposition (3.11) reveals an elegant structure for scalar basis elements. Scalar quantities must be symmetric under the parity transformation (3.23). This enforces the expansion coefficients f ij (±±) and f ij (±∓) to appear very symmetrical as shown in Table 5. In order to exhibit such a symmetry more explicitly, let us introduce 3 × 3 (real) matrices defined by

$$(A_{\pm})_{ij}\equiv f^{ij}_{(\pm\pm)},\qquad(B)_{ij}\equiv f^{ij}_{(+-)},\qquad(B^{T})_{ij}\equiv f^{ij}_{(-+)},\qquad i,j=1,2,3.\tag{4.26}$$

Then the matrices A± are symmetric, i.e. AT ± = A±, but the matrix B is a general 3×3 matrix with no explicit symmetry. The parity transformation (3.23) denoted by P acts on the matrices as

$P:A_{\pm}\leftrightarrow A_{\mp},\qquad P:B\leftrightarrow B^{T}.$ (4.27)

It may be instructive to represent the basis elements in Table 5 in terms of the matrices in (4.26) to illuminate the symmetry structure enforced by the parity symmetry. In the matrix notation, the Ricci scalar in (3.15) reads

$R=4\big{(}{\rm Tr}A_{+}+{\rm Tr}A_{-}\big{)}$.

It is easy to translate the Table 5 into the matrix notation. Surprisingly, it turns out that the 14 basis elements

| I: R4                     ||         ||   Tr  BBT 2 VIII:       ||              |
| ---                       || ---     || ---                       || ---          |
| R2Tr   BBT  II:          ||         || IX: Tr  BBT  Tr   A2 + + ||  A2 −       |
|  R2Tr   A2 III: + + A2 − ||         || X: TrA2 +TrA2 + +         || TrA2 −TrA2 − |
|    A3 IV: RTr + + A3 −   ||         || 2    (BBT ) XI: Tr       ||              |
|   BTA+B V: RTr +          || BA−BT  ||   A+BA−BT  XII: Tr       ||              |
| VI: R detB                ||         ||   BTA2 XIII: Tr +B +      || BA2 −BT     |
| VII: TrA2 +TrA2 −         ||         ||   A4  XIV: Tr A4 − + +   ||              |


Table 3: Matrix representation of the quartic basis elements

listed in Table 3 or Table 5 are not completely independent. There exists one linear relation among the quartic basis elements given by Eq. (D.6). Therefore, the number of linearly independent basis elements for quartic scalars is 13.

The quintic scalars have 90 basis elements, denoted by R0 10,5 in Appendix A of Ref. [35], among which the number of Weyl tensor monomials, denoted by C 0 10,5 in Appendix D, is 19. But their explicit expression has not been displayed in Ref. [35]. Thus we do not know the explicit form of quintic monomials. Nevertheless, our method gives a hint as to how many independent quintic basis elements can exist. It is necessary to count how many quintic matrix polynomials made of the matrices in (4.26) which are parity even. To do this, let us first summarize the quadratic and cubic basis elements in (4.3) and (C.2):

$$Q_{2}=\{R^{2},\text{Tr}\left(A_{+}^{2}+A_{-}^{2}\right),\text{Tr}(BB^{T})\},$$ $$Q_{3}=\{R^{3},R\,\text{Tr}\left(A_{+}^{2}+A_{-}^{2}\right),R\,\text{Tr}(BB^{T}),\text{Tr}\left(A_{+}^{3}+A_{-}^{3}\right),\text{Tr}\left(B^{T}A_{+}B+BA_{-}B^{T}\right),\text{det}B\}.\tag{4.29}$$

Denote the basis in (4.28) as Q1 and the set of basis elements in Table 3 as Q4. Then the quintic basis can be generated by considering the tensor products Q1⊗Q4 and Q2⊗Q3 and newly generated basis Q5 at the quintic order. Since Q1 has the unique element R in (4.28), it is obvious that the tensor products Q1 ⊗ Q4 consists of the set in Table 3 multiplied by R which contains 13 elements. The tensor product Q2 ⊗ Q3 generates new elements which are not overlapped with those in Q1 ⊗ Q4. Their list is

$$Q_{2}\otimes Q_{3}\supset\{{\rm Tr}A_{+}^{2}{\rm Tr}A_{+}^{3}+{\rm Tr}A_{-}^{2}{\rm Tr}A_{-}^{3},\ {\rm Tr}A_{+}^{2}\,{\rm Tr}A_{-}^{3}+{\rm Tr}A_{-}^{2}\,{\rm Tr}A_{+}^{3},\tag{4.30}$$ $${\rm Tr}\left(A_{+}^{2}+A_{-}^{2}\right){\rm Tr}\left(B^{T}A_{+}B+BA_{-}B^{T}\right),\ {\rm Tr}BB^{T}{\rm Tr}\left(A_{+}^{3}+A_{-}^{3}\right),$$ $${\rm Tr}\left(A_{+}^{2}+A_{-}^{2}\right){\rm det}B,\ {\rm Tr}BB^{T}{\rm Tr}\left(B^{T}A_{+}B+BA_{-}B^{T}\right),\ {\rm Tr}BB^{T}{\rm det}B\}.$$

It is not difficult to find the newly generated basis Q5 at the quintic order. They are given by6

$$Q_{5}=\{{\rm Tr}\left(A_{+}^{5}+A_{-}^{5}\right),\,{\rm Tr}\left(B^{T}A_{+}^{3}B+BA_{-}^{3}B^{T}\right),\,{\rm Tr}\left(A_{+}^{2}BA_{-}B^{T}+A_{-}^{2}BA_{+}B^{T}\right),\tag{4.31}$$ $${\rm Tr}\left(BB^{T}A_{+}BB^{T}+B^{T}BA_{-}B^{T}B\right)\}.$$

S 5 1 ∼ S 5 13 : Q1 ⊗ Q4 S 5 19 : TrBBT Tr BT A+B + BA−BT S 5 14 : TrA2 +TrA3 + + TrA2 −TrA3 − S 5 20 : TrBBT detB S 5 15 : TrA2 +TrA3 − + TrA2 −TrA3 + S 5 21 : Tr A5 + + A5 − S 5 16 : Tr A2 + + A2 − Tr BTA+B + BA−BT S 5 22 : Tr BTA3 +B + BA3 −BT S 5 17 : TrBBT Tr A3 + + A3 − S 5 23 : Tr A2 +BA−BT + Tr A2 −BA+BT S 5 18 : Tr A2 + + A2 − detB S 5 24 : Tr BBTA+BBT + BT BA−BT B

Table 4: Matrix representation of the quintic basis elements

The above argument implies that the quintic scalars, not explicitly known yet, have totally 24 basis elements. We summarize the quintic scalar basis in Table 4. But, as the number of independent quartic scalars has been reduced due to the existence of the linear relation (D.6), the number of independent basis elements can be

<sup>6</sup>There is a subtle element: Q odd 5 = Tr B TBA+BA− + BBT A−B T A+ . This is parity even in itself but the odd power of the matrix B. If this combination were allowed at the quintic order, a similar term Tr B TBA+B + B T A−B T B would also be allowed at the quartic order. But this term did not appear at the quartic order. So we rule out Q odd 5 . The result in Table 3 alludes that a term of odd powers of B is only possible in the form of detB because detB = detB T .

further reduced if there exists a similar linear relation among the members in Table 4. We claim that there is such a linear relation between the basis elements, S 5 1 ∼ S 5 24. The linear relation (D.6) for quartic scalars was derived from Eq. (8) in Ref. [35] and such identity can be extended to quintic order [54]. So we expect the number of linearly independent quintic scalars in Table 4 will be 23. It implies that 90 quintic scalars in Ref. [35] obey totally 67 = 90 − 23 linear relations.

Although we will stop at the quintic order, it is straightforward to extend the argument to higher orders. A nontrivial step is to find linear relations (syzygies) between the basis elements such as (D.6) whose existence is guaranteed by the Cayley-Hamilton theorem [54, 55, 56]. In particular, it will be interesting to find a generating function for the basis elements of scalar monomials such as Tables 3 and 4.

### 5 Discussion

We have verified that the irreducible decomposition of the Riemann tensor (3.11) provides a powerful tool for the study of the scalar invariants of the Riemann tensor. Although we have used the decomposition (3.11) for convenience, the true irreducible decomposition of the Riemann tensor must refer to Eq. (3.18), i.e.,

$$R_{abcd}=\vec{f}^{ij}_{(++)}\eta^{i}_{ab}\nu^{j}_{cd}+\vec{f}^{ij}_{(--)}\vec{\eta}^{i}_{ab}\nu^{j}_{cd}+f^{ij}_{(+-)}\big{(}\eta^{i}_{ab}\vec{\eta}^{j}_{cd}+\vec{\eta}^{j}_{ab}\eta^{i}_{cd}\big{)}+\frac{1}{12}R\big{(}\delta_{ac}\delta_{bd}-\delta_{ad}\delta_{bc}\big{)}.\tag{5.1}$$

This decomposition has the following correspondence with the spinor representation and the bivector form on the complex three-dimensional space of self-dual bivectors [32]:

$$\left(\widetilde{A}_{+}\right)_{ij}\leftrightarrow\Psi_{ABCD}\leftrightarrow\Psi^{ij},\qquad\left(\widetilde{A}_{-}\right)_{ij}\leftrightarrow\overline{\Psi}_{ABCD}\leftrightarrow\overline{\Psi}^{ij},\qquad\left(B+iB^{T}\right)_{ij}\leftrightarrow\Phi_{ABCD}\leftrightarrow i\Gamma^{ij},\tag{5.2}$$

where Ae± ij ≡ A± ij − 1 3 δijTrA± = feij (±±) . The corresponding rotor quantities, Ψ and Ψ, are symmetric and trace-free 3 × 3 complex matrices and Γ is a 3 × 3 Hermitian matrix. We have observed that the Riemann polynomial reveals an elegant structure under the parity transformation (3.23). The Riemann polynomials can be classified into two classes: parity even and odd polynomials. The parity even (odd) polynomial is an eigenstate of the parity operator P with eigenvalue +1 (−1). Schematically, it can be stated as

$$Pf(x_{1},\cdots,x_{n})=\pm f(x_{1},\cdots,x_{n})\tag{5.3}$$

where xi's are Riemann monomials such as the members in Table 1 or 2. A parity odd polynomial is called a pseudo-scalar or pseudo-tensor; for example, the Hirzebruch density in (3.19), pseudo-tensors in Eq. (4.16) and a cubic pseudo-scalar in footnote 4. So far we have mainly considered Riemann polynomials that are parity even.

Now we will discuss how to generate a Riemann polynomial which is parity odd, from the parity even polynomials. Since the parity operator P acts on each monomial in the polynomial (5.3), i.e., P f(x1, · · · , xn) = f(P x1, · · · , P xn), it suffices to find independent basis elements at each order which are parity odd. Let us define the pseudo-Riemann tensor

$$\widetilde{R}_{abcd}\equiv\frac{1}{2}\varepsilon_{cdef}R_{abef}\tag{5.4}$$

which can be decomposed as

$$\widetilde{R}_{abcd}=\widetilde{f}^{ij}_{(++)}\eta^{i}_{ab}\eta^{j}_{cd}-\widetilde{f}^{ij}_{(--)}\eta^{i}_{ab}\eta^{j}_{cd}+f^{ij}_{(+-)}\big{(}-\eta^{i}_{ab}\eta^{j}_{cd}+\bar{\eta}^{j}_{ab}\eta^{i}_{cd}\big{)}+\frac{1}{12}R\,\varepsilon_{abcd}.\tag{5.5}$$

Its contraction identically vanishes, e.g., Re ab ≡ Re acbc = 0, that is due to the Bianchi identity (2.7). Since a parity odd Riemann polynomial has to contain only the odd power of the pseudo-Riemann tensor (5.4), it implies that the parity odd Riemann polynomial can be generated by flipping the sign in front of Ae− (or A−) and B (but keeping the sign of BT ) in a parity even Riemann polynomial.

Let us first apply this rule to the scalar basis elements. We denote the set of pseudo-scalar invariants at order n as Qen:

$\tilde{Q}_{1}=4\big{(}{\rm Tr}A_{+}-{\rm Tr}A_{-}\big{)}=0,\qquad$ by Eq. (3.14), (5.6)

$$\bar{Q}_{2}={\rm Tr}\left(A_{+}^{2}-A_{-}^{2}\right),\tag{5.7}$$

$$\tilde{Q}_{3}=\{R\,{\rm Tr}\left(A_{+}^{2}-A_{-}^{2}\right),{\rm Tr}\left(A_{+}^{3}-A_{-}^{3}\right),{\rm Tr}\left(B^{T}A_{+}B-BA_{-}B^{T}\right)\},\tag{5.8}$$

$$\widetilde{Q}_{4}=\{\widetilde{III},\widetilde{IV},\widetilde{V},\widetilde{IX},\widetilde{X},\widetilde{XIII},\widetilde{XIV}\}=R\widetilde{Q}_{3}\bigcup\{\widetilde{IX},\widetilde{X},\widetilde{XIII},\widetilde{XIV}\},\tag{5.9}$$

where the meaning of tildes in the set Qe4 refers to a pseudo-scalar invariant obtained by applying the above rule to the corresponding term in Table 3. Qe2 corresponds to the Hirzebruch density in (3.19). The same rule can be applied to the quintic scalar invariants in Table 4. In particular, S 5 16 generates two pseudo-scalar invariants,

$$\mathrm{Tr}\left(A_{+}^{2}-A_{-}^{2}\right)\mathrm{Tr}\left(B^{T}A_{+}B+B A_{-}B^{T}\right),\quad\mathrm{Tr}\left(A_{+}^{2}+A_{-}^{2}\right)\mathrm{Tr}\left(B^{T}A_{+}B-B A_{-}B^{T}\right).$$

It is obvious that these sets thus obtained are odd under the parity transformation (3.23). In other words, they are pseudo-scalar invariants.

Let us count the number of independent (pseudo-)scalar invariants after including the pseudo-scalars in Qen. Fortunately the counting at lower orders is easy. A notable point is that the parity even and odd polynomials are linearly independent of each other at the same order. However, for higher-order terms, one should note the fact: odd × odd = even and even × odd = odd. At the quadratic order, the total number of independent basis elements is now four. Since the three elements in Qe3 are independent of each other, the total number at the cubic order becomes 9 = 6 + 3. At the quartic order, new elements would be generated from the products, Q1 ⊗ Qe3 and Qe2 ⊗ Qe2. The elements from Q1 ⊗ Qe3 are already included in Qe4 and the product Qe2 ⊗ Qe2 does not generate new elements because Qe2 2 = X − 2V II. But there is an interesting syzygy connecting the elements in Qe4. From the fact that Eq. (D.6) comes from a quartic polynomial of the Weyl tensor and the term R4 cannot be generated from it since Qe1 = 0, we can infer a pseudo-scalar version of Eq. (D.6):7

$$-3R^{2}{\rm Tr}\left(A_{+}^{2}-A_{-}^{2}\right)+32R{\rm Tr}\left(A_{+}^{3}-A_{-}^{3}\right)-192{\rm Tr}\left(A_{+}^{4}-A_{-}^{4}\right)$$ $$+96\left({\rm Tr}(A_{+}^{2}){\rm Tr}(A_{+}^{2})-{\rm Tr}(A_{-}^{2}){\rm Tr}(A_{-}^{2})\right)=0.\tag{5.10}$$

7Therefore, Eqs. (D.6) and (5.10) can be rewritten as the identity

$$\frac{R^{4}}{32}-12R^{2}\mathrm{Tr}A_{\pm}^{2}+128R\mathrm{Tr}A_{\pm}^{3}-768\mathrm{Tr}A_{\pm}^{4}+384\mathrm{Tr}\big(A_{\pm}^{2}\big)\mathrm{Tr}\big(A_{\pm}^{2}\big)=0$$

for any symmetric 3 × 3 matrix A± with R = 8TrA+ = 8TrA−.

Again it can be most easily checked in a diagonalized frame such that A± = diag(a 1 ±, a2 ±, a3 ±) and a 1 + + a 2 + + a 3 + = a 1 − + a 2 − + a 3 −. Since Eq. (5.10) provides a linear relation among the pseudo-scalar invariants in the set Qe4, the number of linearly independent basis elements in the set Qe4 is 6. Thus the total number of independent quartic (pseudo-)scalar invariants is 19 = 13 + 6.

For the quintic order, the situation becomes a bit complicated. Besides the 23 independent quintic scalar invariants in Table 4, it is necessary to include the new invariants from the products, Q1 ⊗Qe4, Q2 ⊗ Qe3, Q3 ⊗ Qe2, Qe2 ⊗ Qe3 and QeW 5 where the last one is the set of quintic Weyl monomials. It is not difficult to determine newly generated basis elements; 6 elements from Q1 ⊗ Qe4, 7 elements from Q2 ⊗ Qe3 and Q3 ⊗ Qe2 and 4 elements from QeW 5 while one even element from Qe2 ⊗ Qe3, Tr A2 + − A2 − Tr BT A+B − BA−BT . Hence 17 odd elements and 1 even elememt are newly generated after including the pseudo-scalars in Qen. However, the 17 odd elements may not be completely independent since it is expected that the quintic order will also give rise to an identity similar to Eq. (5.10) according to the Caley-Hamilton theorem [54, 55, 56]. Therefore we claim that there are totally 40 = 23 + 17 linearly independent quintic (pseudo-)scalar invariants.

It was shown [35] that the quintic scalars have 90 basis elements, among which the number of Weyl tensor monomials is 19.8 But we do not know the explicit form of quintic monomials since their explicit expression has not been displayed in Ref. [35]. Since we have identified 23 linearly independent quintic scalar invariants, we may try to construct 90 basis elements from the 23 linearly independent basis elements. The idea is to use Eq. (4.5) to invert the quintic basis elements expressed in terms of the 't Hooft symbols f ij (±±) and f ij (±∓) into homogeneous polynomials of Riemann tensors, as was done in section 4.1. To do it, it is necessary to use several identities of the 't Hooft symbols in Appendix A. Of course, a computer would be a great help in doing this. If the 23 basis elements exhaust all 90 quintic scalars, our conjecture would be confirmed. It will be more interesting if the parity odd elements discussed above are included. We look forward to reporting some results of studies in this direction in the near future.

It has been well known [5, 12, 20] that, in general, there are 14 (algebraically) independent, second-order, invariants formed from the Riemann tensor Rabcd. However, it does not provide any guidance as to how these invariants may be constructed. An important problem is how much algebraic information that is in the Riemann tensor can be encoded in its polynomial invariants. An "algebraically complete" set means that it must consist of invariants of the lowest possible degree, and also it must be the smallest set which contains the maximum number of independent invariants for any Petrov or Segre type. It was realized [31, 32, 33] that an algebraically complete set should contain more than 14 invariants and hence, in general, be redundant. It was shown in [57] that the set of 16 invariants proposed in [31] is not algebraically complete and even the set of 17 invariants proposed in [33] is missing an essential element although it is algebraically complete. Hence it was suggested in [57, 58, 59] that an algebraically complete set needs at most the equivalent of 18 real invariants with a maximum overall degree of 6. It will be interesting to have the explicit expression of these invariants in terms of the irreducible decomposition (3.11) or (5.1), which may be useful to determine whether the set of 18 invariants proposed in [57] is independent or not. Any progress in this direction will be reported.

Our approach may be generalized to the case with covariant derivatives. The covariant derivative of the

<sup>8</sup>Note that the result in [35] was missing the parity odd elements. We have discussed above how these can be restored.

Riemann curvature tensor is defined by

$$\nabla_{\mu}R_{\nu\lambda ab}=\partial_{\mu}R_{\nu\lambda ab}-\Gamma^{\rho}_{\mu\nu}R_{\rho\lambda ab}-\Gamma^{\rho}_{\mu\lambda}R_{\nu\rho ab}+\omega_{a\rho\mu}R_{\nu\lambda cb}-R_{\nu\lambda a}\omega_{cba}.\tag{5.11}$$

The spin connection can be split into a pair of SU(2)+ and SU(2)− gauge fields according to the Lie algebra splitting (1.2) [36, 37, 40]:

$$\omega_{ab\mu}=A^{(+)i}_{\mu}\eta^{i}_{ab}+A^{(-)i}_{\mu}\bar{\eta}^{i}_{ab}.\tag{5.12}$$

Then the covariant derivative (5.11) can be decomposed as

$$\nabla_{\mu}R_{abcd}=\big{(}\nabla_{\mu}f^{ij}_{(++)}\big{)}\eta^{i}_{ab}\eta^{j}_{cd}+\big{(}\nabla_{\mu}f^{ij}_{(+-)}\big{)}\eta^{i}_{ab}\bar{\eta}^{j}_{cd}+\big{(}\nabla_{\mu}f^{ij}_{(-+)}\big{)}\bar{\eta}^{i}_{ab}\bar{\eta}^{j}_{cd}+\big{(}\nabla_{\mu}f^{ij}_{(--)}\big{)}\bar{\eta}^{i}_{ab}\bar{\eta}^{j}_{cd},\tag{5.13}$$

where the covariant derivatives are given by

$$\nabla_{\mu}f^{ij}_{(\pm\pm)}=\partial_{\mu}f^{ij}_{(\pm\pm)}-2\left(e^{ikl}A^{(\pm)k}_{\mu}f^{lj}_{(\pm\pm)}+e^{jkl}A^{(\pm)k}_{\mu}f^{il}_{(\pm\pm)}\right),$$ $$\nabla_{\mu}f^{ij}_{(\pm\mp)}=\partial_{\mu}f^{ij}_{(\pm\mp)}-2\left(e^{ikl}A^{(\pm)k}_{\mu}f^{lj}_{(\pm\mp)}+e^{jkl}A^{(\mp)k}_{\mu}f^{il}_{(\pm\mp)}\right).\tag{5.14}$$

The second Bianchi identity takes an interesting form:

$$\nabla_{e}R_{abcd}+\nabla_{a}R_{bcd}+\nabla_{b}R_{acad}=0$$ $$\Leftrightarrow\eta^{i}_{ab}\nabla_{b}f^{ij}_{(+)}=\eta^{i}_{ab}\nabla_{b}f^{ij}_{(-)},\quad\eta^{i}_{ab}\nabla_{b}f^{ij}_{(-)}=\eta^{i}_{ab}\nabla_{b}f^{ij}_{(+-)}.\tag{5.15}$$

One can see that the decomposition of the covariant derivative (5.13) has essentially the same form as that of the curvature tensor (3.11) except that the coefficients are replaced by the covariant derivatives (5.14). Therefore incorporating the covariant derivative of the curvature tensor into a Riemann polynomial would not entail great difficulties.

Although the signature of the metric is irrelevant for the linear dependence of scalar invariants of the Riemann tensor, its dimensionality becomes important. For example, in the three-dimensional space, the Weyl tensor identically vanishes. As a result, there is a linear relation quadratic in the Riemann tensor:

$$R_{a b c d}^{2}-4R_{a b}^{2}+R^{2}=0.$$

Moreover, the number of independent differential invariants crucially depends on the dimension of space. In d-dimensions, it is kwown to be [12]

$$I(d)\equiv\frac{d^{2}(d^{2}-1)}{12}-\left(\begin{array}{c}{{d}}\\ {{2}}\end{array}\right)=\frac{d+3}{2}\left(\begin{array}{c}{{d}}\\ {{3}}\end{array}\right)$$

and this number becomes I(4) = 14, I(5) = 40 and I(6) = 90 in four, five and six dimensions, respectively. It was shown [60] that, in six dimensions, there are eight scalar invariants cubic in the Riemann tensor (the list is exactly the same as the four-dimensional case listed in section 4.2) but there is no linear relation between these invariants unlike the four-dimensional case. The maximum dimension of space in which linear relation can exist among invariants of order n in the Riemann tensor is given by dmax = 2n−1 [60]. Thus it is expected

that there will be linear relations for quartic (n = 4) scalar invariants in six dimensions. It will be interesting to understand more closely the algebraic structure of scalar invariants in six dimensions.

In six dimensions, there also exists a global isomorphism between a six-dimensional Lorentz group and a classical Lie group:

$Spin(6)\cong SU(4)$.

Therefore it is possible to devise a six-dimensional version of the 't Hooft symbols using the isomorphism between the chiral so(6) Lorentz algebra and the su(4) Lie algebra [61]. Since the chiral and anti-chiral (or the fundamental and anti-fundamental) representations of so(6) (or su(4)) must be distinct, there are two kinds of 't Hooft symbols, η a AB and η¯ a AB, with a = 1, · · · , 15, A, B = 1, · · · , 6, and they satisfy algebraic identities similar to the four-dimensional case. The six-dimensional Riemann curvature tensor can be classified into two classes:

$$\mathbb{A}:R^{(+)}_{ABCD}=f^{ab}_{(++)}\eta^{a}_{AB}\eta^{b}_{CD},\tag{5.17}$$

$$\mathbb{B}:R^{(-)}_{ABCD}=f^{ab}_{(--)}\bar{\eta}^{a}_{AB}\bar{\eta}^{b}_{CD}.\tag{5.18}$$

This expression may be very useful for studying the algebraic properties of six-dimensional scalar invariants. In particular, it was argued [61] that the existence of two classes and their splitting into A and B would be related to the mirror symmetry of Calabi-Yau manifolds. It will be interesting to find any relationship between the scalar invariants of each class. We hope to address this issue in the near future too.

## Acknowledgments

This research was performed using Mathematica (www.wolfram.com) and the add-on package MathSymbolica (www.mathsymbolica.com). This work was supported by the National Research Foundation of Korea (NRF) with grant number NRF-2018R1D1A1B0705011314 (HSY). We acknowledge the hospitality at APCTP where part of this work was done.

## A 't Hooft symbols

The explicit components of the 't Hooft symbols η i ab and η i ab for i = 1, 2, 3 are given by

$$\eta^{i}_{ab}=\varepsilon^{i4ab}+\delta^{ia}\delta^{4b}-\delta^{ib}\delta^{4a},$$ (A.1) $$\overline{\eta}^{i}_{ab}=\varepsilon^{i4ab}-\delta^{ia}\delta^{4b}+\delta^{ib}\delta^{4a}$$

with ε 1234 = 1. They satisfy the following relations

$$\eta^{(\pm)i}_{ab}=\pm\frac{1}{2}\varepsilon_{ab}{}^{cd}\eta^{(\pm)i}_{cd},$$ (A.2)

$$\eta^{(\pm)i}_{ab}\eta^{(\pm)i}_{cd}=\delta_{ac}\delta_{bd}-\delta_{ad}\delta_{bc}\pm\varepsilon_{abcd},$$ (A.3)

$$\varepsilon_{abcd}\eta^{(\pm)i}_{de}=\mp(\delta_{ce}\eta^{(\pm)i}_{ab}+\delta_{ca}\eta^{(\pm)i}_{bc}-\delta_{eb}\eta^{(\pm)i}_{ac}),$$ (A.4)

$\eta^{(\pm)i}_{ab}\eta^{(\mp)j}_{ab}=0$, (A.5)

$$\eta^{(\pm)i}_{ac}\eta^{(\pm)j}_{bc}=\delta^{ij}\delta_{ab}+\varepsilon^{ijk}\eta^{(\pm)k}_{ab},$$ (A.6)

$$\eta^{(\pm)i}_{ac}\eta^{(\mp)j}_{bc}=\eta^{(\pm)i}_{bc}\eta^{(\mp)j}_{ac},$$ (A.7)

$$\varepsilon^{ijk}\eta^{(\pm)j}_{ab}\eta^{(\pm)k}_{cd}=\delta_{ac}\eta^{(\pm)i}_{bd}-\delta_{ad}\eta^{(\pm)i}_{bc}-\delta_{bc}\eta^{(\pm)i}_{ad}+\delta_{bd}\eta^{(\pm)i}_{ac},$$ (A.8)

where η (+)i ab ≡ η i ab and η (−)i ab ≡ η i ab.

If we introduce two families of 4 × 4 matrices defined by

$$[\tau_{+}^{i}]_{ab}\equiv\frac{1}{2}\eta_{ab}^{i},\qquad[\tau_{-}^{i}]_{ab}\equiv\frac{1}{2}\overline{\eta}_{ab}^{i},$$ (A.9)

the matrices in (A.9) provide two independent spin s = 3 2 representations of su(2) Lie algebra. Explicitly, they are given by

τ 1 + = 1 2 0 0 0 1 0 0 1 0 0 −1 0 0 −1 0 0 0 , τ 2 + = 1 2 0 0 −1 0 0 0 0 1 1 0 0 0 0 −1 0 0 , τ 3 + = 1 2 0 1 0 0 −1 0 0 0 0 0 0 1 0 0 −1 0 , τ 1 − = 1 2 0 0 0 −1 0 0 1 0 0 −1 0 0 1 0 0 0 , τ 2 − = 1 2 0 0 −1 0 0 0 0 −1 1 0 0 0 0 1 0 0 , τ 3 − = 1 2 0 1 0 0 −1 0 0 0 0 0 0 −1 0 0 1 0 

according to the definition (A.1). The relations in (A.6) and (A.7) immediately show that τ i ± satisfy su(2) Lie algebras, i.e.,

$$[\tau^{i}_{\pm},\tau^{j}_{\pm}]=-\varepsilon^{ijk}\tau^{k}_{\pm},\qquad[\tau^{i}_{\pm},\tau^{j}_{\mp}]=0.$$ (A.10)

## B Don't panic!

Here we will analytically prove the identities (4.1) and (4.2) using the decomposition (3.25). In order to simplify the calculation, it is convenient to choose pairs with the most contractions and perform the calculation with them. So we will show (4.1) by choosing the following pair:

Ra1a2b1b2Ra2b1b2e1 Rc1c2d1d2Rc2d1d2e2 Re1a1e2c1 = Ra1a2b1b2Ra2b1b2e1 f i1i2 (++)η i1 c1c2 η i2 d1d2 + f i1i2 (−−) η¯ i1 c1c2 η¯ i2 d1d2 f j1j2 (++)η j1 c2d1 η j2 d2e2 + f j1j2 (−−) η¯ j1 c2d1 η¯ j2 d2e2 Re1a1e2c1 = Ra1a2b1b2Ra2b1b2e1 δ i1j1δc1d1 + ε i1j1k1 η k1 c1d1 δ i2j2δd1e2 + ε i2j2k2 η¯ k2 d1e2 f i1i2 (++)f j1j2 (++) + δ i1j1δc1d1 + ε i1j1k1η¯ k1 c1d1 δ i2j2δd1e2 + ε i2j2k2η¯ k2 d1e2 f i1i2 (−−) f j1j2 (−−) +[η i1 η¯ j1 η i2 η¯ j2 ]c1e2 f i1i2 (++)f j1j2 (−−) + [¯η i1 η j1η¯ i2 η j2 ]c1e2 f i1i2 (−−) f j1j2 (++)Re1a1e2c1 . (B.1)

Note that

[η i1 η¯ j1η i2 η¯ j2 ]c1e2 = [η i1 η i2 η¯ j1η¯ j2 ]c1e2 = [(δ i1i2 1 + ε i1i2i3 η i3 )(δ j1j21 + ε j1j2j3η¯ j3 )]c1e2 = [δ i1i2 δ j1j21 + δ j1j2ε i1i2i3 η i3 + δ i1i2ε j1j2j3η¯ j3 + ε i1i2i3 ε j1j2j3η i3 η¯ j3 ]c1e2

and a similar formula holds for the matrix [¯η i1 η j1 η¯ i2 η j2 ]c1e2 . Now it is easy to see that Eq. (B.1) identically vanishes when recalling Eq. (3.12) and the fact that [η iη¯ j ]c1e2 is a symmetric matrix by Eq. (A.7). Although it is straightforward, the proof of Eq. (4.2) by hand requires a little algebra:

2Ra1a2b1b2Rc1c2a1d1Rd2b1d1a2Rb2d2c1c2 = −2 · 4 3 f i1i2 (++)f i1j1 (++)f k1k2 (++)f l1l2 (++) + f i1i2 (−−) f i1j1 (−−) f k1k2 (−−) f l1l2 (−−) ε j1l1k1 ε i2l2k2 , −Ra1a2b1b2Rc1c2d1a1Rd2a2c2c1Rb1b2d1d2 = −4 3 f i1i2 (++)f i1i2 (++) − f i1i2 (−−) f i1i2 (−−) 2 + 2 · 4 3 f i1i2 (++)f i1j2 (++)f j1i2 (++)f j1j2 (++) + f i1i2 (−−) f i1j2 (−−) f j1i2 (−−) f j1j2 (−−) .

It is convenient to arrange the remaining two terms using the identity (2.7):

4Ra1a2b1b2Rc1c2d1a1Rd2a2b1c1 Rd1b2d2c2 + Rd2d1b2c2 = 4Ra1a2b1b2Rc1c2d1a1Rd2a2b1c1Rb2d2c2d1 = 43 f i1i2 (++)f i1j1 (++)f k1k2 (++)f l1l2 (++) + f i1i2 (−−) f i1j1 (−−) f k1k2 (−−) f l1l2 (−−) ε j1l1k1ε i2l2k2 −2 · 4 3 f i1i2 (++)f i1i2 (++)f j1j2 (−−) f j1j2 (−−) + 43 f i1i2 (++)f i1i2 (++) + f j1j2 (−−) f j1j2 (−−) f k1k2 (++)δ k1k2 2 −2 · 4 3 f i1i2 (++)f j1i2 (++)f i1j1 (++) + f i1i2 (−−) f j1i2 (−−) f i1j1 (−−) f k1k2 (++)δ k1k2 , (B.2)

where we have used the identity (3.13). Combining all these terms leads to the identity (4.2).

## C Cubic identities for a general Riemannian manifold

The identity (4.22) becomes trivial for an Einstein manifold which satisfies the equation Rab = 1 4Rδab and the identity (4.23) reduces to

$$R_{a c b d}R_{c e d f}R_{e a f b}=\frac{1}{16}R^{3}-\frac{3}{8}R R_{a b c d}R_{a b c d}+\frac{1}{2}R_{a b c d}R_{c d e f}R_{e f a b}.$$

Therefore, in order to prove that the identities (4.22) and (4.23) are the only linear relations existent in the cubic terms, we will consider a general Riemannian manifold and represent the eight cubic monomials using the decomposition (3.11):

RRabRab = R3 4 + 16Rfij (+−) f ij (+−) , RabRbcRca = R3 16 + 12Rfij (+−) f ij (+−) − 32 2f i1i2 (+−) f i2i3 (+−) f i3i1 (+−) − 3f i1i1 (+−) f i2i3 (+−) f i3i2 (+−) + f i1i1 (+−) f i2i2 (+−) f i3i3 (+−) , RacRbdRabcd = R3 16 + 4Rfij (+−) f ij (+−) + 32 2f i1i2 (+−) f i2i3 (+−) f i3i1 (+−) − 3f i1i1 (+−) f i2i3 (+−) f i3i2 (+−) + f i1i1 (+−) f i2i2 (+−) f i3i3 (+−) +32 f i1i2 (++)f i1i3 (+−) f i2i3 (+−) + f i1i2 (−−) f i3i1 (+−) f i3i2 (+−) , RRabcdRabcd = 16R f ij (++)f ij (++) + 2f ij (+−) f ij (+−) + f ij (−−) f ij (−−) , (C.1) RabRacdeRbcde = 4R f ij (++)f ij (++) + 2f ij (+−) f ij (+−) + f ij (−−) f ij (−−) +64 f i1i2 (++)f i1i3 (+−) f i2i3 (+−) + f i1i2 (−−) f i3i1 (+−) f i3i2 (+−) , RabcdRcdefRefab = 192 f i1i2 (++)f i1i3 (+−) f i2i3 (+−) + f i1i2 (−−) f i3i1 (+−) f i3i2 (+−) +64 f i1i2 (++)f i1i3 (++)f i2i3 (++) + f i1i2 (−−) f i1i3 (−−) f i2i3 (−−) , RacbdRcedfReafb = R3 16 − 6R f ij (++)f ij (++) + f ij (−−) f ij (−−) + 32 f i1i2 (++)f i1i3 (++)f i2i3 (++) + f i1i2 (−−) f i1i3 (−−) f i2i3 (−−) +32 2f i1i2 (+−) f i2i3 (+−) f i3i1 (+−) − 3f i1i1 (+−) f i2i3 (+−) f i3i2 (+−) + f i1i1 (+−) f i2i2 (+−) f i3i3 (+−) .

One can see that the above 7 monomials are expressed in terms of only 5 types of terms besides the term R3 , listed below. All the cubic monomials are symmetric under the interchange (3.23) since they are scalars. The six independent basis elements of the cubic Riemann monomials are given by

R 3 , R f ij (++)f ij (++) + f ij (−−) f ij (−−) , Rfij (+−) f ij (+−) , f i1i2 (++)f i1i3 (++)f i2i3 (++) + f i1i2 (−−) f i1i3 (−−) f i2i3 (−−) , f i1i2 (++)f i1i3 (+−) f i2i3 (+−) + f i1i2 (−−) f i3i1 (+−) f i3i2 (+−) , (C.2) 2f i1i2 (+−) f i2i3 (+−) f i3i1 (+−) − 3f i1i1 (+−) f i2i3 (+−) f i3i2 (+−) + f i1i1 (+−) f i2i2 (+−) f i3i3 (+−) = 6 detf ij (+−) ,

where detf ij (+−) is the determinant of the 3×3 matrix f ij (+−) . 9 The first three basis elements in (C.2) correspond to the quadratic ones (4.3) multiplied by R. The last basis in (C.2) consists of three terms which are self-

<sup>9</sup>Using the matrix notation (4.26), detf ij (+−) can be written as detB = 1 3 TrB 3− 1 2 TrB TrB 2+ 1 6 TrB 3 . This expression appeared in Eq. (4) of Ref. [30] and was used to reduce independent invariants.

symmetric under the parity transformation (3.23). Thus they could form independent basis separately, but they must appear with that combination because they come from the product of Ricci tensors, RabRbcRca. It is also clear from the fact that such combination forms detf ij (+−) . This proves that the cubic scalars have only six independent basis elements. Replacing the 5 types of terms by the cubic monomials leads to the identities (4.22) and (4.23). There is no more linear relation. Our approach identifies the independent basis of Riemann monomials without any ambiguity.

Now we list the result for the expansion of second-rank cubic monomials in Table 1. For notational simplicity, we will use the matrix notation in (4.26):

A : R 2Rab = R3 4 δab − 2R 2Bi1i2 η i1 η¯ i2 ab, B : RRacRbc = R3 16 + 4R TrBBT δab − 2R Tr B 2 + (B T ) 2 − 2 TrB 2 η i1 η¯ i1 ab − R 2B − 8R (B T ) 2 − TrBBT i1i2 η i1 η¯ i2 ab, C : RabR 2 cd = R3 16 + 4R Tr BBT δab − R2 2 B + 32Tr BBT B i1i2 η i1 η¯ i2 ab, D : RacRbdRcd = R3 64 + 3R Tr BBT − 48 detB δab − 3 2 R Tr B 2 + (B T ) 2 − 2 TrB 2 η i1 η¯ i1 ab − 3 8 R 2B − 6R (B T ) 2 − TrB BT − 16BBT B + 24Tr BBT B i1i2 η i1 η¯ i2 ab, E : RRcdRacbd = R3 16 + 4R Tr BBT δab + 2R Tr B 2 + (B T ) 2 − 2 TrB 2 η i1 η¯ i1 ab −4R (A+B + BA−) + 2(B T ) 2 − 2(TrB)B T i1i2 η i1 η¯ i2 ab, F : RceRdeRacbd = R3 64 + 3R Tr BBT − 48 detB δab + R Tr B 2 + (B T ) 2 − 2 TrB 2 η i1 η¯ i1 ab +4Tr B 2 + (B T ) 2 − 2TrB B (A+ + A−) η i1 η¯ i1 ab + R2 8 B − 2R A+B + BA− + 2(B T ) 2 − 2TrB BT i1i2 η i1 η¯ i2 ab + 8TrB (B TA+ + A−B T ) − 8TrB (A+B T + B T A−) + 8Tr(BA+ + B TA−)B T −8(B T A+B T + B TA−B T ) + 8 A+(B T ) 2 + (B T ) 2A− − (B T ) 2A+ − A−(B T ) 2 + 8Tr BBT B +4 TrB 2 (A+ + A−) − 2Tr B 2 + (B T ) 2 (A+ + A−) − 16BBT B η i1 η¯ i2 ab,

i1i2

G : RacRdeRbecd = R3 64 + RTr BBT + 48 detB + 8Tr B TA+B + BA−B T δab − R2 8 B + R A+B + BA− + 4 TrB 2 (A+ + A−) − 2Tr B 2 + (B T ) 2 (A+ + A−) −8TrB A+B T + B TA− + 8 A+(B T ) 2 + (B T ) 2A− − 8Tr BBT B + 16BBT B i1i2 η i1 η¯ i2 ab +8ε i1i2i3 BBTA+ i1i2 η i3 ab + B TBA− i1i2 η¯ i3 ab , H : RRaecdRbecd = 4RTr A 2 + + A 2 − + 2BBT δab − 8R A+B + BA− i1i2 η i1 η¯ i2 ab, I : RabR 2 cdef = 4RTr A 2 + + A 2 − + 2BBT δab − 32Tr A 2 + + A 2 − + 2BBT Bi1i2 η i1 η¯ i2 ab, J : RacRbedfRcedf = RTr A 2 + + A 2 − + 2BBT + 16Tr B T A+B + BA−B T δab −8Tr B 2 + (B T ) 2 − 2TrB B (A+ + A−) η i1 η¯ i1 ab − 2R A+B + BA− i1i2 η i1 η¯ i2 ab, −8 Tr A 2 + + A 2 − B + 2TrB B TA+ + A−B T − 2 (B T ) 2A+ + A−(B T ) 2 + 2Tr BA+ + B TA− B −2 B TA+B T + B T A−B T + 2Tr BBT B i1i2 η i1 η¯ i2 ab +16ε i1i2i3 BBTA+ i1i2 η i3 ab + B T BA− i1i2 η¯ i3 ab , K : RefRaecdRbfcd = RTr A 2 + + A 2 − + 2BBT + 16Tr B T A+B + BA−B T δab +8Tr B 2 + (B T ) 2 − 2TrB B (A+ + A−) η i1 η¯ i1 ab − 2R A+B + BA− i1i2 η i1 η¯ i2 ab +8 Tr A 2 + + A 2 − B + 2TrB B TA+ + A−B T − 2 (B T ) 2A+ + A−(B T ) 2 + 2Tr BA+ + B TA− B −2 A 2 +B + BA2 − − 2 B T A+B T + B TA−B T + 2Tr BBT B − 4BBTB i1i2 η i1 η¯ i2 ab, L : RefRacbdRcedf = R3 64 + RTr BBT + 48 detB + 8Tr B TA+B + BA−B T δab + R 2 Tr B 2 + (B T ) 2 − 2 TrB 2 η i1 η¯ i1 ab − 4Tr B 2 + (B T ) 2 − 2TrB B (A+ + A−) η i1 η¯ i1 ab − R2 8 B − R A+B + BA− − R B 2 + (B T ) 2 − 2(TrB) B T η i1 η¯ i2 ab

T

T

−8 TrB B T A+ + A−B T − (B T ) 2A+ + A−(B T ) 2 + Tr BA+ + B T A− B T + A 2 +B + BA2 − − B T A+B T + B TA−B T + 3Tr BBT B − 2BBTB + 2A+BA− i1i2 η i1 η¯ i2 ab,

i1i2

$$\begin{array}{c}{{M:R_{e f}R_{a c d e}R_{b c d e}=\left(R\mathrm{Tr}\big(A_{+}^{2}+A_{-}^{2}+2B B^{T}\big)+16\mathrm{Tr}\big(B^{T}A_{+}B+B A_{-}B^{T}\big)\right)\delta_{a b}}}\\ {{-2\Big(R\big(A_{+}B+B A_{-}\big)+8\big(B B^{T}B+A_{+}B A_{-}\big)\Big)_{i_{1}i_{2}}\left(\eta^{i_{1}}\bar{\eta}^{i_{2}}\right)_{a b},}}\end{array}$$

N : RagcdRbgefRcdef = 16 Tr A 3 + + A 3 − + 3Tr B TA+B + BA−B T δab −32 A 2 +B + BA2 − + BBTB + A+BA− i1i2 η i1 η¯ i2 ab, O : RaecgRbfdgRcdef = R3 64 − 3 2 RTr A 2 + + A 2 − + 48 detB + 8Tr A 3 + + A 3 − δab − R2 8 B − R A+B + BA− − 4Tr A 2 + + A 2 − B + 4 TrB 2 (A+ + A−) i1i2 η i1 η¯ i2 ab +41 2 Tr B 2 + (B T ) 2 (A+ + A−) + 2TrB A+B T + B TA− −2 A 2 +B + BA2 − + A+(B T ) 2 + (B T ) 2A− i1i2 η i1 η¯ i2 ab, P : RaebgRcdefRcdf g = − RTr A 2 + + A 2 − + 2BBT + 16Tr B TA+B + BA−B T δab −8Tr B 2 + (B T ) 2 − 2TrB B (A+ + A−) η i1 η¯ i1 ab − 2R (A+B + BA−)i1i2 η i1 η¯ i2 ab, +8 Tr A 2 + + A 2 − B − 2TrB B TA+ + A−B T − 2Tr BA+ + B TA− B T + 2Tr BBT B +2 A 2 +B + BA2 − + (B T ) 2A+ + A−(B T ) 2 + B T A+B T + B TA−B T + 2A+BA− i1i2 η i1 η¯ i2 ab.

Note that the second-rank cubic tensors in Table 1 are parity even, so they must be invariant under the parity transformation (4.27). One can quickly check it by noting that the parity transformation acts on P : η i1 η¯ i2 ab → η¯ i1 η i2 ab = η i2 η¯ i1 ab. The second-rank cubic monomials in Table 1 are symmetric with respect to (a ↔ b) except in G and J which contain an anti-symmetric part as was shown above. Although the expansion is much more complicated compared to the scalar case, it turns out that terms that would appear in the scalar case reappear with the factor 1 4 δab, and novel terms that do not appear in the scalar case (or should disappear in the scalar case) appear with the factor (η iη¯ j )ab. Indeed, δab and (η iη¯ j )ab are the only symmetric tensors constructed from the product of 't Hooft symbols. The latter is trace-free due to Eq. (A.5). In particular, (η iη¯ i )ab is a diagonal matrix given by

$$(\eta^{i}\bar{\eta}^{i})_{ab}=-\eta^{i}_{ac}\bar{\eta}^{i}_{bc}=-\left(\delta_{ab}-4\delta_{a4}\delta_{b4}\right)=-\left(\begin{array}{cccc}1&0&0&0\\ 0&1&0&0\\ 0&0&1&0\\ 0&0&0&-3\end{array}\right).$$ (C.3)

We found that there are two algebraic relations for the second-rank cubic tensors in Table 1. We list them

below:

R 2Rab − 4RabR 2 cd − 8RacRdeRbecd − 2RRacdeRbecd + RabR 2 cdef + 4RefRaecdRbfcd +8RefRaecdRbcdf + 4RacRbedfRcedf + 8RaecgRbfdgRcdef − 4RagcdRbgefRcdef = 0, (C.4) RRacRbc − 2RacRbdRcd + RRcdRacbd − 2RceRdeRacbd − 6RacRdeRbecd − RRaecdRbecd +4RefRacdeRbcdf + 2RefRaecdRbfcd − 2RefRacbdRcedf + 3RacRbedfRcedf +4RaecgRbfdgRcdef − 2RagcdRbgefRcdef − RaebgRcdefRcdf g = 0. (C.5)

It is natural to expect that there exist more than two linear relations between the second-rank cubic tensors in Table 1 since contracting the free indices a and b has to reproduce the eight cubic scalars which obey the syzygy relations (4.22) and (4.23). However we found that there exist 14 linearly independent second-rank cubic tensors using a computer algorithm.10 This means that Eqs. (C.4) and (C.5) exhaust all possible linear relations for the second-rank cubic tensors in Table 1. It also implies that Eqs. (C.4) and (C.5) have to reproduce the syzygies (4.22) and (4.23) when contracting a and b. It can be checked by eliminating RaecgRbfdgRcdef and RacRbedfRcedf from Eqs. (C.4) and (C.5), respectively, and then combining them together to obtain

R 2Rab − 2RRacRbc + 4RacRbdRcd − 4RabR 2 cd − 2RRcdRacbd + 4RceRdeRacbd +4RacRdeRbecd + RabR 2 cdef + 4RefRacbdRcedf − 2RacRbedfRcedf + 2RaebgRcdefRcdf g = 0,(C.6) 3R 2Rab − 4RRacRbc + 8RacRbdRcd − 12RabR 2 cd − 4RRcdRacbd + 8RceRdeRacbd −2RRaecdRbecd + 8RefRacdeRbcdf + 4RefRaecdRbfcd + 3RabR 2 cdef + 8RefRacbdRcedf −4RagcdRbgefRcdef + 8RaecgRbfdgRcdef + 4RaebgRcdefRcdf g = 0. (C.7)

Combining the above equations after contracting a and b reproduces the cubic identities (4.22) and (4.23).

<sup>10</sup>The expression for these 14 basis elements is quite complicated and not illuminating, so will not be displayed here. But we can e-mail the result to those who request it.

# D Quartic identities for a general Riemannian manifold

We present the expansion of the 26 quartic monomials in Table 2 using the decomposition (3.11) for a general Riemannian manifold:

A : R 4 = 256 f i1i1 (++) + f i1i1 (−−) 4 , B : R 2RabRab = R4 4 + 16R 2 f i1i2 (+−) 2 , C : RRabRbcRca = R4 16 + 12R 2 f i1i2 (+−) 2 − 32R 2f i1i2 (+−) f i2i3 (+−) f i3i1 (+−) − 3f i1i1 (+−) f i2i3 (+−) f i3i2 (+−) + f i1i1 (+−) f i2i2 (+−) f i3i3 (+−) , D : (RabRab) 2 = R4 16 + 8R 2 f i1i2 (+−) 2 + 256 f i1i2 (+−) 2 f i3i4 (+−) 2 , E : RabRbcRcdRda = R4 64 + 6R 2 f i1i2 (+−) 2 − 32R 2f i1i2 (+−) f i2i3 (+−) f i3i1 (+−) − 3f i1i1 (+−) f i2i3 (+−) f i3i2 (+−) + f i1i1 (+−) f i2i2 (+−) f i3i3 (+−) i1i2 f i1i3 f i4i2 f i4i3 ,

(+−)

$$\begin{array}{c}{{+192\left(f_{(+-)}^{i_{1}i_{2}}\right)^{2}\left(f_{(+-)}^{i_{3}i_{4}}\right)^{2}-128f_{0}}}\\ {{}}\\ {{R R_{+}R_{-}\cdot R_{-}\cdot\cdot}}\end{array}$$

F : RRabRcdRacbd = R4 16 + 4R 2 f i1i2 (+−) 2 + 32R 2f i1i2 (+−) f i2i3 (+−) f i3i1 (+−) − 3f i1i1 (+−) f i2i3 (+−) f i3i2 (+−) + f i1i1 (+−) f i2i2 (+−) f i3i3 (+−) + f i1i2 (+−) f i3i2 (+−) f i1i3 (++) + f i2i1 (+−) f i2i3 (+−) f i1i3 (−−) ,

(+−)

(+−)

(+−)

G : RabRceRedRacbd = R4 64 + 2R 2 f i1i2 (+−) 2 + 8R 2f i1i2 (+−) f i2i3 (+−) f i3i1 (+−) − 3f i1i1 (+−) f i2i3 (+−) f i3i2 (+−) + f i1i1 (+−) f i2i2 (+−) f i3i3 (+−) +2 f i1i2 (+−) f i3i2 (+−) f i1i3 (++) + f i2i1 (+−) f i2i3 (+−) f i1i3 (−−) − 64 f i1i2 (+−) 2 f i3i4 (+−) 2 + 128f i1i2 (+−) f i1i3 (+−) f i4i2 (+−) f i4i3 (+−) −32 f i1i2 (+−) f i2i1 (+−) f i3i4 (+−) f i3i4 (++) − f i1i1 (+−) f i2i2 (+−) f i3i4 (+−) f i3i4 (++) +2f i1i1 (+−) f i2i3 (+−) f i4i2 (+−) f i3i4 (++) − 2f i1i2 (+−) f i2i3 (+−) f i4i1 (+−) f i3i4 (++) −32 f i1i2 (+−) f i2i1 (+−) f i3i4 (+−) f i3i4 (−−) − f i1i1 (+−) f i2i2 (+−) f i3i4 (+−) f i3i4 (−−) +2f i1i1 (+−) f i3i2 (+−) f i2i4 (+−) f i3i4 (−−) − 2f i2i1 (+−) f i3i2 (+−) f i1i4 (+−) f i3i4 (−−) , H : R 2RabcdRabcd = 16R 2 f i1i2 (++)2 + 2 f i1i2 (+−) 2 + f i1i2 (−−) 2 ,

f i1i3 (−−) ,

2 + f i1i2 (−−)

2 ,

I : RRabRacdeRbcde = 4R 2 f i1i2 (++)2 + 2 f i1i2 (+−) 2 + f i1i2 (−−) 2 + 64R f i1i2 (+−) f i3i2 (+−) f i1i3 (++) + f i2i1 (+−) f i2i3 (+−) J : RabRabRcdefRcdef = 4R 2 f i1i2 (++)2 + 2 f i1i2 (+−) 2 + f i1i2 (−−) 2 + 256 f i3i4 (+−) 2 f i1i2 (++)2 + 2 f i1i2 (+−)

K : RabRbcRdefaRdefc

= R 2 f i1i2 (++)2 + 2 f i1i2 (+−) 2 + f i1i2 (−−) 2 + 32R f i1i2 (+−) f i3i2 (+−) f i1i3 (++) + f i2i1 (+−) f i2i3 (+−) f i1i3 (−−) +64 f i3i4 (+−) 2 f i1i2 (++)2 + 2 f i1i2 (+−) 2 + f i1i2 (−−) 2 +128 f i1i2 (+−) f i2i1 (+−) f i3i4 (+−) f i3i4 (++) − f i1i1 (+−) f i2i2 (+−) f i3i4 (+−) f i3i4 (++) +2f i1i1 (+−) f i2i3 (+−) f i4i2 (+−) f i3i4 (++) − 2f i1i2 (+−) f i2i3 (+−) f i4i1 (+−) f i3i4 (++) +128 f i1i2 (+−) f i2i1 (+−) f i3i4 (+−) f i3i4 (−−) − f i1i1 (+−) f i2i2 (+−) f i3i4 (+−) f i3i4 (−−) +2f i1i1 (+−) f i3i2 (+−) f i2i4 (+−) f i3i4 (−−) − 2f i2i1 (+−) f i3i2 (+−) f i1i4 (+−) f i3i4 (−−) ,

- L : RabRcdRacefRbdef
= R 2 f i1i2 (++)2 + 2 f i1i2 (+−) 2 + f i1i2 (−−) 2 + 32R f i1i2 (+−) f i3i2 (+−) f i1i3 (++) + f i2i1 (+−) f i2i3 (+−) f i1i3 (−−) −64 f i3i4 (+−) 2 f i1i2 (++)2 + 2 f i1i2 (+−) 2 + f i1i2 (−−) 2 −128 f i1i2 (+−) f i2i1 (+−) f i3i4 (+−) f i3i4 (++) − f i1i1 (+−) f i2i2 (+−) f i3i4 (+−) f i3i4 (++) +2f i1i1 (+−) f i2i3 (+−) f i4i2 (+−) f i3i4 (++) − 2f i1i2 (+−) f i2i3 (+−) f i4i1 (+−) f i3i4 (++) −128 f i1i2 (+−) f i2i1 (+−) f i3i4 (+−) f i3i4 (−−) − f i1i1 (+−) f i2i2 (+−) f i3i4 (+−) f i3i4 (−−) +2f i1i1 (+−) f i3i2 (+−) f i2i4 (+−) f i3i4 (−−) − 2f i2i1 (+−) f i3i2 (+−) f i1i4 (+−) f i3i4 (−−) +128 f i1i2 (+−) f i3i2 (+−) f i1i4 (++)f i3i4 (++) + 2f i1i2 (+−) f i1i3 (+−) f i4i2 (+−) f i4i3 (+−) + f i2i1 (+−) f i2i3 (+−) f i1i4 (−−) f i3i4 (−−) ,

M : RabRcdRaebfRcedf

= R4 64 + 2R 2 f i1i2 (+−) 2 + 12R 2f i1i2 (+−) f i2i3 (+−) f i3i1 (+−) − 3f i1i1 (+−) f i2i3 (+−) f i3i2 (+−) + f i1i1 (+−) f i2i2 (+−) f i3i3 (+−) +192 f i1i2 (+−) 2 f i3i4 (+−) 2 + 16 f i1i2 (+−) f i2i1 (+−) f i3i4 (+−) f i3i4 (++) − f i1i1 (+−) f i2i2 (+−) f i3i4 (+−) f i3i4 (++) +2f i1i1 (+−) f i2i3 (+−) f i4i2 (+−) f i3i4 (++) − 2f i1i2 (+−) f i2i3 (+−) f i4i1 (+−) f i3i4 (++) +16 f i1i2 (+−) f i2i1 (+−) f i3i4 (+−) f i3i4 (−−) − f i1i1 (+−) f i2i2 (+−) f i3i4 (+−) f i3i4 (−−) +2f i1i1 (+−) f i3i2 (+−) f i2i4 (+−) f i3i4 (−−) − 2f i2i1 (+−) f i3i2 (+−) f i1i4 (+−) f i3i4 (−−) +64 f i1i2 (+−) f i3i2 (+−) f i1i4 (++)f i3i4 (++) + 2f i1i3 (+−) f i2i4 (+−) f i1i2 (++)f i3i4 (−−) −2f i1i2 (+−) f i1i3 (+−) f i4i2 (+−) f i4i3 (+−) + f i2i1 (+−) f i2i3 (+−) f i1i4 (−−) f i3i4 (−−) ,

N : RabRcdRaecfRbedf

= R 2 f i1i2 (++)2 + 2 f i1i2 (+−) 2 + f i1i2 (−−) 2 + 32R f i1i2 (+−) f i3i2 (+−) f i1i3 (++) + f i2i1 (+−) f i2i3 (+−) f i1i3 (−−) +128 f i1i2 (++)f i3i4 (−−) f i1i3 (+−) f i2i4 (+−) + f i1i2 (+−) f i1i3 (+−) f i4i2 (+−) f i4i3 (+−) ,

O : RRabcdRcdefRefab

$$=64R\left(f_{(+)}^{i1i_{2}}f_{(+)}^{i1i_{3}}f_{(++)}^{i2i_{3}}+3f_{(+)}^{i1i_{2}}f_{(+-)}^{i1i_{2}}f_{(-)}^{i2i_{3}}+3f_{(-)}^{i1i_{3}}f_{(+-)}^{i2i_{1}}f_{(+-)}^{i1i_{3}}+f_{(--)}^{i1i_{2}}f_{(--)}^{i1i_{3}}f_{(--)}^{i2i_{3}}\right),$$

$$P:RR_{abcd}R_{acbf}R_{acbf}=\frac{R^{4}}{16}-6R^{2}\left(\left(f_{(+)}^{i_{1}i_{2}}\right)^{2}+\left(f_{(-)}^{i_{1}i_{2}}\right)^{2}\right)$$

$$\begin{array}{l}{{+32R\left(\left(2f_{(+-)}^{i_{1}i_{2}}f_{(+-)}^{i_{2}i_{3}}f_{(+-)}^{i_{3}i_{1}}-3f_{(+-)}^{i_{1}i_{1}}f_{(+-)}^{i_{2}i_{3}}f_{(+-)}^{i_{3}i_{2}}+f_{(+-)}^{i_{1}i_{1}}f_{(+-)}^{i_{2}i_{2}}f_{(+-)}^{i_{3}i_{3}}\right)\right)}}\\ {{+\left(f_{(++)}^{i_{1}i_{2}}f_{(++)}^{i_{1}i_{3}}f_{(++)}^{i_{2}i_{3}}+f_{(-)}^{i_{1}i_{2}}f_{(--)}^{i_{1}i_{3}}f_{(--)}^{i_{2}i_{3}}\right)\right),}}\end{array}$$

Q : RabRacbdRef gcRef gd

= R 2 f i1i2 (++)2 + 2 f i1i2 (+−) 2 + f i1i2 (−−) 2 + 64 f i3i4 (+−) 2 f i1i2 (++)2 + 2 f i1i2 (+−) 2 + f i1i2 (−−) 2 −128 f i1i2 (+−) f i2i1 (+−) f i3i4 (+−) f i3i4 (++) − f i1i1 (+−) f i2i2 (+−) f i3i4 (+−) f i3i4 (++) +2f i1i1 (+−) f i2i3 (+−) f i4i2 (+−) f i3i4 (++) − 2f i1i2 (+−) f i2i3 (+−) f i4i1 (+−) f i3i4 (++) −128 f i1i2 (+−) f i2i1 (+−) f i3i4 (+−) f i3i4 (−−) − f i1i1 (+−) f i2i2 (+−) f i3i4 (+−) f i3i4 (−−)

+2f i1i1 (+−) f i3i2 (+−) f i2i4 (+−) f i3i4 (−−) − 2f i2i1 (+−) f i3i2 (+−) f i1i4 (+−) f i3i4 (−−) 

$$+128\left(f_{(+-)}^{i_{1}i_{2}}f_{(+-)}^{i_{3}i_{2}}f_{(++)}^{i_{1}i_{4}}f_{(++)}^{i_{3}i_{4}}+2f_{(++)}^{i_{1}i_{2}}f_{(--)}^{i_{3}i_{4}}f_{(+-)}^{i_{1}i_{3}}f_{(+-)}^{i_{2}i_{4}}+f_{(+-)}^{i_{2}i_{1}}f_{(+-)}^{i_{2}i_{3}}f_{(--)}^{i_{1}i_{4}}f_{(--)}^{i_{3}i_{4}}\right),$$

R : RabRcdefRagefRbgcd

= 16R f i1i2 (++)f i1i3 (++)f i2i3 (++) + 3f i1i3 (++)f i1i2 (+−) f i3i2 (+−) + 3f i1i3 (−−) f i2i1 (+−) f i2i3 (+−) + f i1i2 (−−) f i1i3 (−−) f i2i3 (−−) +256 f i1i2 (++)f i2i3 (++)f i3i4 (+−) f i1i4 (+−) + f i1i2 (++)f i3i4 (−−) f i1i3 (+−) f i2i4 (+−) +f i1i2 (+−) f i1i3 (+−) f i4i2 (+−) f i4i3 (+−) + f i1i2 (−−) f i2i3 (−−) f i4i3 (+−) f i4i1 (+−) ,

S : RabRcedfRegfaRgcbd = R4 64 − R2 2 3 f i1i2 (++)2 − 2 f i1i2 (+−) 2 + 3 f i1i2 (−−) 2 +8R 2f i1i2 (+−) f i2i3 (+−) f i3i1 (+−) − 3f i1i1 (+−) f i2i3 (+−) f i3i2 (+−) + f i1i1 (+−) f i2i2 (+−) f i3i3 (+−) + f i1i2 (++)f i1i3 (++)f i2i3 (++) − f i1i3 (++)f i1i2 (+−) f i3i2 (+−) − f i1i3 (−−) f i2i1 (+−) f i2i3 (+−) + f i1i2 (−−) f i1i3 (−−) f i2i3 (−−) −32 f i3i4 (+−) 2 f i1i2 (++)2 + f i1i2 (−−) 2 + 64 f i1i2 (+−) f i3i2 (+−) f i1i4 (++)f i3i4 (++) + f i2i1 (+−) f i2i3 (+−) f i1i4 (−−) f i3i4 (−−) −32 f i1i2 (+−) f i2i1 (+−) f i3i4 (+−) f i3i4 (++) − f i1i1 (+−) f i2i2 (+−) f i3i4 (+−) f i3i4 (++) +2f i1i1 (+−) f i2i3 (+−) f i4i2 (+−) f i3i4 (++) − 2f i1i2 (+−) f i2i3 (+−) f i4i1 (+−) f i3i4 (++) −32 f i1i2 (+−) f i2i1 (+−) f i3i4 (+−) f i3i4 (−−) − f i1i1 (+−) f i2i2 (+−) f i3i4 (+−) f i3i4 (−−) +2f i1i1 (+−) f i3i2 (+−) f i2i4 (+−) f i3i4 (−−) − 2f i2i1 (+−) f i3i2 (+−) f i1i4 (+−) f i3i4 (−−) ,

T : RabcdRabcd2 = 256 f i1i2 (++)2 + 2 f i1i2 (+−) 2 + f i1i2 (−−) 2 2 , f i3i4 2 f i1i2 2 + f i1i2 2 +

U : RabcdRabceRf ghdRf ghe = 256 (+−) (++)(+−) f i1i2 (−−) 2 +64 f i1i2 (++) 2 f i3i4 (++) 2 + 2 f i1i2 (++) 2 f i3i4 (−−) 2 + f i1i2 (−−) 2 f i3i4 (−−) 2 +256 f i1i2 (++)f i2i3 (++)f i3i4 (+−) f i1i4 (+−) + 2f i1i2 (++)f i3i4 (−−) f i1i3 (+−) f i2i4 (+−) + f i1i2 (−−) f i2i3 (−−) f i4i3 (+−) f i4i1 (+−)

$$V:R_{a b c d}R_{c d e f}R_{e f g h}R_{g h a b}$$

= 256 f i1i2 (++)f i1i3 (++)f i2i4 (++)f i3i4 (++) + 4f i1i2 (++)f i2i4 (++)f i1i3 (+−) f i4i3 (+−) + 4f i1i2 (++)f i3i4 (−−) f i1i3 (+−) f i2i4 (+−) +2f i1i2 (+−) f i1i3 (+−) f i4i2 (+−) f i4i3 (+−) + 4f i1i2 (−−) f i2i4 (−−) f i3i1 (+−) f i3i4 (+−) + f i1i2 (−−) f i1i3 (−−) f i2i4 (−−) f i3i4 (−−) ,

,

W : RabcdRabefRceghRdf gh

= −64 f i1i2 (++) 2 f i3i4 (++) 2 − 2 f i1i2 (++) 2 f i3i4 (−−) 2 + f i1i2 (−−) 2 f i3i4 (−−) 2 +128 f i1i2 (++)f i1i3 (++)f i2i4 (++)f i3i4 (++) + 4f i1i2 (++)f i2i4 (++)f i1i3 (+−) f i4i3 (+−) + 4f i1i2 (++)f i3i4 (−−) f i1i3 (+−) f i2i4 (+−) +2f i1i2 (+−) f i1i3 (+−) f i4i2 (+−) f i4i3 (+−) + 4f i1i2 (−−) f i2i4 (−−) f i3i1 (+−) f i3i4 (+−) + f i1i2 (−−) f i1i3 (−−) f i2i4 (−−) f i3i4 (−−) ,

X : RabcdRefabRgcheRgdhf = R 2 f i1i2 (++)2 + 2 f i1i2 (+−) 2 + f i1i2 (−−) 2 −16R f i1i2 (++)f i1i3 (++)f i2i3 (++) + f i1i3 (++)f i1i2 (+−) f i3i2 (+−) + f i1i3 (−−) f i2i1 (+−) f i2i3 (+−) + f i1i2 (−−) f i1i3 (−−) f i2i3 (−−) −64 f i1i2 (++) 2 f i3i4 (++) 2 + f i1i2 (++) 2 f i3i4 (+−) 2 + f i1i2 (−−) 2 f i3i4 (+−) 2 + f i1i2 (−−) 2 f i3i4 (−−) 2 −128 f i1i2 (+−) f i2i1 (+−) f i3i4 (+−) f i3i4 (++) − f i1i1 (+−) f i2i2 (+−) f i3i4 (+−) f i3i4 (++) +2f i1i1 (+−) f i2i3 (+−) f i4i2 (+−) f i3i4 (++) − 2f i1i2 (+−) f i2i3 (+−) f i4i1 (+−) f i3i4 (++) −128 f i1i2 (+−) f i2i1 (+−) f i3i4 (+−) f i3i4 (−−) − f i1i1 (+−) f i2i2 (+−) f i3i4 (+−) f i3i4 (−−) +2f i1i1 (+−) f i3i2 (+−) f i2i4 (+−) f i3i4 (−−) − 2f i2i1 (+−) f i3i2 (+−) f i1i4 (+−) f i3i4 (−−) +128 f i1i2 (++)f i1i3 (++)f i2i4 (++)f i3i4 (++) + f i1i2 (++)f i2i4 (++)f i1i3 (+−) f i4i3 (+−) +f i1i2 (−−) f i2i4 (−−) f i3i1 (+−) f i3i4 (+−) + f i1i2 (−−) f i1i3 (−−) f i2i4 (−−) f i3i4 (−−) ,

Y : RacbdRcedfRegfhRgahb = 64 f i3i4 (+−) 2 f i1i2 (++) 2 + 3 f i1i2 (+−) 2 + f i1i2 (−−) 2 −32 f i1i2 (++)f i1i3 (++)f i2i4 (++)f i3i4 (++) − 4f i2i1 (+−) f i3i1 (+−) f i2i4 (++)f i3i4 (++) − 12f i1i2 (++)f i1i3 (+−) f i2i4 (+−) f i3i4 (−−) +2f i1i2 (+−) f i1i3 (+−) f i4i2 (+−) f i4i3 (+−) − 4f i1i2 (+−) f i1i3 (+−) f i2i4 (−−) f i3i4 (−−) + f i1i2 (−−) f i1i3 (−−) f i2i4 (−−) f i3i4 (−−) +48 f i1i2 (++) 2 f i3i4 (++) 2 + 2 f i1i2 (++) 2 f i3i4 (−−) 2 + f i1i2 (−−) 2 f i3i4 (−−) 2 , Z : RacbdReafbRgehcRf gdh = 7 512 R 4 − 1 8 R 2 13 f i1i2 (++) 2 − 16 f i1i2 (+−) 2 + 13 f i1i2 (−−) 2 +R 12f i1i2 (++)f i1i3 (++)f i2i3 (++) − 16f i2i1 (+−) f i3i1 (+−) f i2i3 (++) + 7f i1i1 (+−) f i2i2 (+−) f i3i3 (+−) − 21f i1i1 (+−) f i2i3 (+−) f i3i2 (+−) +14f i1i2 (+−) f i2i3 (+−) f i3i1 (+−) − 16f i1i2 (+−) f i1i3 (+−) f i2i3 (−−) + 12f i1i2 (−−) f i1i3 (−−) f i2i3 (−−) −44 f i1i2 (+−) f i2i1 (+−) f i3i4 (+−) f i3i4 (++) − f i1i1 (+−) f i2i2 (+−) f i3i4 (+−) f i3i4 (++) +2f i1i1 (+−) f i2i3 (+−) f i4i2 (+−) f i3i4 (++) − 2f i1i2 (+−) f i2i3 (+−) f i4i1 (+−) f i3i4 (++) −44 f i1i2 (+−) f i2i1 (+−) f i3i4 (+−) f i3i4 (−−) − f i1i1 (+−) f i2i2 (+−) f i3i4 (+−) f i3i4 (−−) +2f i1i1 (+−) f i3i2 (+−) f i2i4 (+−) f i3i4 (−−) − 2f i2i1 (+−) f i3i2 (+−) f i1i4 (+−) f i3i4 (−−) −8 5f i1i2 (++)f i1i3 (++)f i2i4 (++)f i3i4 (++) − 16f i1i2 (+−) f i3i2 (+−) f i1i4 (++)f i3i4 (++) − 32f i1i2 (++)f i1i3 (+−) f i2i4 (+−) f i3i4 (−−) −16f i2i1 (+−) f i2i3 (+−) f i1i4 (−−) f i3i4 (−−) + 5f i1i2 (−−) f i1i3 (−−) f i2i4 (−−) f i3i4 (−−) +4 5 f i1i2 (++) 2 f i3i4 (++) 2 + 16 f i1i2 (++) 2 f i3i4 (−−) 2 + 16 f i1i2 (+−) 2 f i3i4 (+−) 2 + 5 f i1i2 (−−) 2 f i3i4 (−−) 2 .

Note that all terms are symmetric under the interchange (3.23) since scalar quantities are parity even.

For some terms in G, K, L, M, Q, S, X and Z, we have the identity

$$\begin{array}{ll}&(f_{(+-)}^{i_{1}i_{1}}-f_{(--)}^{i_{2}i_{4}})\left(f_{(+-)}^{i_{1}i_{2}}f_{(+-)}^{i_{2}i_{4}}-f_{(+-)}^{i_{1}i_{1}}f_{(+-)}^{i_{2}i_{2}}f_{(+-)}^{i_{2}i_{4}}+2f_{(+-)}^{i_{1}i_{2}}f_{(+-)}^{i_{2}i_{4}}f_{(+-)}^{i_{2}}-2f_{(+-)}^{i_{1}i_{2}}f_{(+-)}^{i_{2}i_{4}}f_{(+-)}^{i_{1}i_{1}}\right)\\ &=&-2\Big{(}f_{(+-)}^{i_{3}}\delta^{ij}-f_{(--)}^{ij}\delta^{ij}\Big{)}\text{det}f_{(+-)}^{ij}=0.\end{array}$$ (D.1)

Since (D.1) is odd under the parity transformation (3.23), its vanishing can be easily understood from this property. This means that such terms can be written as − 1 4R detf ij (+−) . It is interesting to compare this expression for detf ij (+−) with the result in Eq. (C.2). Using the identity (D.1), it is straightforward to identity the basis elements for the quartic monomials in Table 2 which superficially look independent. The result is summarized in Table 5. The first 6 basis elements, from I to V I, are simply coming from the cubic ones (C.2) multiplied

| 2   f || 2   ||   f  || i1i2 || i3i4 || R4   || I:      || VIII: || (+−) || (+−)   || 2   || R2  f || 2   f || 2  || 2 +  || i1i2  ||   f   || i3i4  || i1i2  ||   f || i1i2  ||     ||      ||      ||      ||      ||      ||      ||      ||      ||      ||      ||      ||     ||     |
| ---    || ---  || ---  || ---  || ---  || ---  || ---     || ---   || ---  || ---    || ---  || ---    || ---     || ---  || ---   || ---   || ---   || ---   || ---   || --- || ---   || --- || ---  || ---  || ---  || ---  || ---  || ---  || ---  || ---  || ---  || ---  || ---  || --- || --- |
| II:    || IX:  || (+−) || (+−) || (++) || (−−) || R2   f || 2   || 2 + || 2   f || 2 + || 2   f || 2      ||      ||       ||       ||       ||       ||       ||     ||       ||     ||      ||      ||      ||      ||      ||      ||      ||      ||      ||      ||      ||     ||     |
| i1i2   ||   f  || i1i2 ||   f  || i1i2 || i3i4 ||   f     || i1i2  || i3i4 || III:   || X:   || (−−)   || (−−)    || (−−) || (++)  || (++)  || (++)  ||       ||       ||     ||       ||     ||      ||      ||      ||      ||      ||      ||      ||      ||      ||      ||      ||     ||     |
|  f    ||     || i1i2 || i1i3 || i2i3 || i1i2 || i1i3    || i2i3  || i1i2 || i1i3   || i4i2 || i4i3   || IV:     || R    || (++)f || (++)f || +     || f     || f     || f   || XI:   || f   || f    || f    || f    || (++) || (−−) || (−−) || (−−) || (+−) || (+−) || (+−) || (+−) ||  f ||    |
| i1i2   || i1i3 || i2i3 || i1i2 || i3i1 || i3i2 || i1i2    || i3i4  || i1i3 || i2i4   || V:   || R      || (++)f   || f    || +     || f     || f     || f     || XII:  || f   || (++)f || f   || f    || (+−) || (+−) || (−−) || (+−) || (+−) || (−−) || (+−) || (+−) ||      ||      ||     ||     |
| ij     || i1i2 || i2i4 || i1i3 || i4i3 || i1i2 || i2i4    || i3i1  || i3i4 || VI:    || R    || detf   || XIII:   || f    || (++)f || (++)f || f     || +     || f     || f   || f     || f   || (+−) || (+−) || (+−) || (−−) || (−−) || (+−) || (+−) ||      ||      ||      ||      ||     ||     |
| 2   f || 2   ||   f  || i1i2 || i3i4 || i1i2 || i1i3    || i2i4  || i3i4 || i1i2   || i1i3 || i2i4   || i3i4    || VII: || XIV:  || f     || (++)f || (++)f || (++)f || +   || f     || f   || f    || f    || (−−) || (−−) || (−−) || (−−) || (−−) || (++) || (++) ||      ||      ||     ||     |


Table 5: The 14 quartic basis elements

by R. The remaining 8 elements are newly generated in the quartic order.

We will show that the 26 quartic monomials in Table 2 can be represented by using only 13 linearly independent basis elements. This means that the 14 basis elements listed in Table 5 are not completely independent. We will explain later how one linear relation among the quartic scalars arises. This implies that there must be 13 linear relations among the quartic monomials. A. Harvey found 6 such relations using the fact [50] that an (n + 1) index object anti-symmetrized on an n-dimensional manifold vanishes identically. However his results contain several errors and we will correct them here. We find that there are 7 more linear relations in addition to the 6 relations found by Harvey. We can find such linear relations by replacing the quartic basis elements in Table 5 in favor of the corresponding quartic monomials in Table 2. We first list the 12 linear relations between the Riemann monomials in Table 2.

(a) : −R 4 + 9R 2RabRab − 14RRabRbcRca − 6 RabRab2 + 12RabRbcRcdRda −6RRabRcdRacbd + 12RabRceRedRacbd = 0, (b) : − R4 4 + 2R 2RabRab − 2RRabRbcRca − 2RRabRcdRacbd − 1 4 R 2RabcdRabcd + RRabRacdeRbcde = 0, (c) : −2R 4 + 15R 2RabRab − 16RRabRbcRca − 12RRabRcdRacbd − 3RabRabRcdefRcdef +12RabRbcRadefRcdef = 0,

(d) : − 11 2 R 4 + 87 2 R 2RabRab − 56RRabRbcRca − 18 RabRab2 + 36RabRbcRcdRda −18RRabRcdRacbd − 3 2 R 2RabcdRabcd + 3 2 RabRabRcdefRcdef + 12RabRcdRaecfRbedf −12RabRcdRaebfRcedf + 6RabRcdRacefRbdef = 0, (e) : 5 4 R 4 − 9R 2RabRab + 8RRabRbcRca + 6RRabRcdRacbd + 3 4 R 2RabcdRabcd −RRabcdRcdefRefab + 2RRabcdRaecfRbedf = 0, (f) : −2R 4 + 15R 2RabRab − 28RRabRbcRca + 24RabRbcRcdRda − 3RabRabRcdefRcdef −24RabRcdRaebfRcedf + 12RabRacbdRcef gRdef g = 0, (g) : − R4 2 + 3R 2RabRab − 8RRabRbcRca + 4RRabRcdRacbd + 8RabRbcRcdRda + 1 2 R 2RabcdRabcd

−8RabRcdRaebfRcedf − RabRabRcdefRcdef − 4RabRcdRacefRbdef − RRabcdRcdefRefab +4RabRcdefRcdgaRef gb = 0,

- (h) : 4R 4 − 30R 2RabRab + 32RRabRbcRca + 6 (RabRab) 2 − 12RabRbcRcdRda +18RRabRcdRacbd + 3 2 R 2RabcdRabcd − 6RabRcdRacefRbdef − 3 2 RRabcdRcdefRefab + 12RabRcedfRadcgRbfeg = 0,
- (i) : −5R 4 + 36R 2RabRab − 64RRabRbcRca + 48RabRbcRcdRda − 48RabRcdRaebfRcedf −3 (RabcdRabcd) 2 + 12RabcdRabceRdhf gRehf g = 0,

${(j):\;R^4-6R^2R_{ab}R_{ab}+16RR_{ab}R_{bc}R_{ca}-16R_{ab}R_{bc}R_{cd}R_{da}-8RR_{ab}R_{cd}R_{abcd}-\frac{1}{2}R^2R_{abcd}R_{abcd}}$

${+4R_{ab}R_{cd}R_{acef}R_{bdef}+16R_{ab}R_{cd}R_{abgf}R_{cgf}+RR_{abcd}R_{cdef}R_{efab}+\frac{1}{2}\left(R_{abcd}R_{abcd}\right)^2}$

${+4R_{abcd}R_{abef}R_{cogb}R_{abf}-R_{abcd}R_{cdef}R_{efab}R_{gabab}-2R_{abcd}R_{abef}R_{cogb}R_{gabf}=0,}$

23. 

(k) : − 23 6 R 4 + 28R 2RabRab − 128 3 RRabRbcRca − 8 (RabRab) 2 + 32RabRbcRcdRda −R 2RabcdRabcd + 4RabRabRcdefRcdef − 32RabRcdRaebfRcedf − 3 2 (RabcdRabcd) 2 +8RacbdRcedfRegfhRagbh + RabcdRcdefRef ghRghab = 0,

(l) : 17 12 R 4 − 12R 2RabRab − 128 3 RRabRbcRca − 6 (RabRab) 2 + 84RabRbcRcdRda +72RRabRcdRacbd + 5 2 R 2RabcdRabcd − 20RabRcdRacefRbdef + 8RabRabRcdefRcdef −104RabRcdRaebfRcedf − 6RRabcdRcdefRefab − 13 4 (RabcdRabcd) 2 + 13 2 RabcdRcdefRef ghRghab − 3RabcdRabefRceghRghdf + 32RacbdRaebfRchegRdhf g = 0.

Our results (a), (b) and (c) precisely reproduce Eqs. (11), (9), and (10) in Ref. [50], respectively.11 Unfortunately, Eqs. (15), (17), (18), and (19) in Ref. [50] contain errors too.12 For example, Eq. (15) in Ref. [50] should read as

$$-\frac{5}{4}R^{4}+\frac{39}{4}R^{2}R_{ab}R_{ab}-12RR_{ab}R_{bc}R_{ca}-3\big{(}R_{ab}R_{ab}\big{)}^{2}+6R_{ab}R_{bc}R_{cd}R_{da}$$ $$-5RR_{ab}R_{cd}R_{acbd}-\frac{1}{4}R^{2}R_{ab}R_{abcd}+\frac{1}{4}R_{ab}R_{ab}R_{cdef}R_{cdef}+2R_{ab}R_{bc}R_{adef}R_{cdef}$$ (D.2) $$+2R_{ab}R_{cd}R_{acef}R_{bogf}-2R_{ab}R_{cd}R_{abf}R_{acbf}+R_{ab}R_{cd}R_{acf}R_{bdef}=0.$$

In particular, Eq. (15) in Ref. [50] was missing the term, − 1 4R2RabcdRabcd. The correct equation (D.2) can simply be obtained by adding (c) and (d) and dividing by 6. Since Eq. (17) in Ref. [50] used the incorrect equation (15), it is incorrect too. The correct forms of Eqs. (17) and (19) are given by, respectively,13

(17) : R 4 − 6R 2RabRab + 5RRabRbcRca + 6RabRceRedRacbd + 3 2 RRabRcdeaRcdeb +3RabRbcadRef gcRef gd − 3RabRcdefRef gaRgbcd + 6RabRcedfRegfaRgcbd = 0, (D.3) (19) : − 5 48 R 4 + 1 2 R 2R 2 ab − 1 3 RRabRbcRca + 1 16 R 4 abcd − RabRcdefRef gaRgbcd +2RabRcedfRegfaRgcbd + RabRbcadRef gcRgdef + RacbdRcedfRegfhRagbh −2RabcdRabefRcgehRdgfh − 2RacbdRaebfRchegRdhf g + 1 8 RabcdRcdefRef ghRghab +RabcdRabefRceghRghdf − RabcdRabceRdhf gRf geh = 0. (D.4)

Eq. (D.3) can be reproduced from our results by considering the combination, 1 4 (f)− 3 4 (g)+ 1 2 (h)+ 1 2 (a)+ 3 2 (b). Using 12 linear equations (a) ∼ (l), Eq. (D.4) can be further reduced as

$$-\frac{1}{4}R^{4}+R^{2}R_{ab}R_{ab}+R^{4}_{ab}-2R_{ab}R_{bc}R_{cd}R_{da}-2R_{ab}R_{cd}R_{efac}R_{efbd}+2R_{abcd}R_{cefl}R_{egfl}R_{gabb}$$

$$-4R_{abcd}R_{efb}R_{fgh}R_{gbc}+\frac{3}{2}R_{abcd}R_{abe}R_{cefl}R_{gabd}-R_{abcd}R_{abc}R_{fabd}R_{hefg}=0.$$ (D.5)

Using the notation (4.26), Eqs. (D.4) and (D.5) are equally written as

$$\frac{R^{4}}{16}-12R^{2}{\rm Tr}\left(A_{+}^{2}+A_{-}^{2}\right)+128R{\rm Tr}\left(A_{+}^{3}+A_{-}^{3}\right)-768{\rm Tr}\left(A_{+}^{4}+A_{-}^{4}\right)$$ $$+384\left({\rm Tr}(A_{+}^{2}){\rm Tr}(A_{+}^{2})+{\rm Tr}(A_{-}^{2}){\rm Tr}(A_{-}^{2})\right)=0.$$ (D.6)

The reason why the matrix B does not appear in (D.6) is that Eqs. (D.4) and (D.5) originated from a quartic polynomial of Weyl tensors. The validity of the linear relation (D.6) may be understood by the fact that the

<sup>11</sup>Eq. (11) in Ref. [50] contains a sign error: · · · − 9R 2RabRab + R 4 → · · · + 9R 2RabRab − R 4 .

<sup>12</sup>We used Mathematica (www.wolfram.com) and the add-on package MathSymbolica (www.mathsymbolica.com) for calculation of the quartic Riemann monomials, A ∼ Z, and the linear relations, (a) ∼ (l). We verified the results by numerical tests using randomly generated numbers for the coefficients f ij (±±) and f ij (±∓) , and hence, we believe that our results are error-free.

<sup>13</sup>Eq. (19) in Ref. [50] was derived using Eq. (18), but Eq. (18) contains typographic errors. The rectified version must read as −2R 2R 2 abcd → +2R 2R 2 abcd and − 64 3 RRabRbcRca → + 64 3 RRabRbcRca.

four elements, III, IV, X and XIV , in Table 5 can be shown to be implicitly connected by this relationship. We have confirmed that Eq. (D.4) cannot be derived as a linear combination of the 12 equations, (a) ∼ (l), by checking all possible cases out of 26 terms. This means that Eq. (D.4) must be regarded as a new linear relation in addition to the 12 relations, (a) ∼ (l). It is quite revealing to see that Eq. (D.6) is an identity for general symmetric 3 × 3 matrices A± satisfying the property TrA+ = TrA− = R 8 . It can be most easily checked in a diagonalized frame such that A± = diag(a 1 ±, a2 ±, a3 ±) and a 1 + + a 2 + + a 3 + = a 1 − + a 2 − + a 3 −. Since Eq. (D.6) provides one more linear relation among the quartic basis elements in Table 5, the number of linearly independent basis elements for quartic scalars is 13.

Note added. The above linear relations, (D.4), (D.5), and (D.6), have been derived from the identity Rab [abRcd cdRef efRgh gh] = 0 whose expansion is very complicated [50]. But we found that Eq. (D.6) can be rewritten as P − 6S + 3X = RRabcdRcedfReafb − 6RabRcedfRegfaRgcbd + 3RabcdRefabRgcheRgdhf = 0 using only the three members in Table 2.

### References

- [1] R. Gautreau and J. L. Anderson, Phys. Lett. A 25 (1967) 291.
- [2] W. Israel, Phys. Rev. 164 (1967) 1776.
- [3] G. F. R. Ellis and B. G. Schmidt, Gen. Rel. Grav. 10 (1979) 989.
- [4] A. Z. Petrov, *Einstein Spaces*, Pergamon, Oxford (1969).
- [5] R. Penrose and W. Rindler, *Spinors and space-time*, Vol. 2, Cambridge Univ. Press, Cambridge (1986).
- [6] J. Pleba ´nski and J. Stachel, Einstein Tensor and Spherical Symmetry, J. Math. Phys. 20 (1968) 269.
- [7] C. G. B. McIntosh, J. M. Foyster and A. W.-C. Lun, The classification of the Ricci and Pleba ´nski tensors in general relativity using Newman-Penrose formalism, J. Math. Phys. 22 (1981) 2620.
- [8] E. Zakhary and J. Carminati, A New Algorithm for the Segre Classification of the Trace-Free Ricci Tensor, Gen. Rel. Grav. 36 (2004) 1015.
- [9] J. Ehler and W. Kundt, Exact Solutions of the Gravitational Field Equations, in *Gravitation: An Introduction to Current Research*, edited by L. Witten, John Wiley & Sons, New York (1962).
- [10] A. Karlhede, A review of the geometrical equivalence of metrics in general relativity, Gen. Rel. Grav. 12 (1980) 693.
- [11] A. Coley, S. Hervik and N. Pelavas, Spacetimes characterized by their scalar curvature invariants, Class. Quantum Grav. 26 (2009) 025013.
- [12] S. Weinberg, *Gravitation and Cosmology*, John Wiley & Sons, New York (1972).

- [13] H. Stephani, D. Kramer, M. MacCallum, C. Hoenselaers and E. Herlt, *Exact Solutions of Einstein's Field Equations*, 2nd ed., Cambridge Univ. Press, Cambridge (2003).
- [14] G. W. Gibbons, Quantum field theory in curved spacetime, in *General Relativity: An Einstein centenary survey* edited by S. W. Hawking and W. Isreal, Cambridge Univ. Press, Cambridge (1979).
- [15] B. S. DeWitt, Quantum gravity: the new synthesis, in *General Relativity: An Einstein centenary survey* edited by S. W. Hawking and W. Israel, Cambridge Univ. Press, Cambridge (1979).
- [16] G. A. Vilkovisky, Effective action in quantum gravity, Class. Quantum Grav. 9 (1992) 895.
- [17] P. Amsterdamski, A. L. Berkin and D. J. O'Connor, b8 'Hamidew' coefficient for a scalar field, Class. Quantum Grav. 6 (1989) 1981.
- [18] M. A. H. MacCallum, Computer algebra in gravity research, Living Rev. Rel. 21 (2018) 6.
- [19] J. M. Mart´ın-Garc´ıa, R. Portugal and L. R. U. Manssur, The Invar tensor package, Comp. Phys. Commun. 177 (2007) 640.
- [20] C. N. Haskins, On the invariants of quadratic differential forms, Trans. Am. Math. Soc. 3 (1902) 71.
- [21] V. V. Narlikar and K. R. Karmarkar, The scalar invariants of a general gravitational metric, Proc. Indian Acad. Sci. A 29 (1948) 91.
- [22] A. Harvey, On the algebraic invariants of the four-dimensional Riemann tensor, Class. Quantum Grav. 7 (1990) 715.
- [23] J. G´eh´eniau and R. Debever, Les invariants de courboure de l'space de Riemann `a quatre dimensions, Bull. Acad. Roy. Belg., Cl. des Sc. XLII (1956) 114.
- [24] J. G´eh´eniau, Les invariants de courboure des espaces Riemanniens de la relativit´e, Bull. Acad. Roy. Belg., Cl. des Sc. XLII (1956) 252.
- [25] R. Debever, Etude g´eom´etrique du tenseur de Riemann-Christoffel des ´ espaces de Riemann `a quatre dimensions, Bull. Acad. Roy. Belg., Cl. des Sc. XLII (1956) 313, 608.
- [26] L. Witten, Invariants of General Relativity and the Classification of Spaces, Phys. Rev. 113 (1959) 357.
- [27] J. L. Safko and L. Witten, Some Properties of Cylindrically Symmetric Einstein-Maxwell Fields, J. Math. Phys. 12 (1971) 257.
- [28] P. J. Greenberg, The algebra of the Riemann curvature tensor in general relativity: Preliminaries, Stud. Appl. Math. 51 (1972) 277.
- [29] G. Sobczyk, Space-time algebra approach to curvature, J. Math. Phys. 22 (1981) 333.

- [30] G. E. Sneddon, On the algebraic invariants of the four-dimensional Riemann tensor, Class. Quantum Grav. 3 (1986) 1031.
- [31] J. Carminati and R. G. McLenaghan, Algebraic invariants of the Riemann tensor in a four-dimensional Lorentzian space, J. Math. Phys. 32 (1991) 3135.
- [32] G. E. Sneddon, The identities of the algebraic invariants of the four-dimensional Riemann tensor, J. Math. Phys. 37 (1996) 1059.
- [33] E. Zakhary and C. G. B. McIntosh, A Complete Set of Riemann Invariants, Gen. Rel. Grav. 29 (1997) 539.
- [34] S. Bonanos, A New Spinor Identity and the Vanishing of Certain Riemann Tensor Invariants, Gen. Rel. Grav. 30 (1998) 653.
- [35] S. A. Fulling, R. C. King, B. G. Wybourne and C. J. Cummins, Normal forms for tensor polynomials: I. The Riemann tensor, Class. Quantum Grav. 9 (1992) 1151.
- [36] J. J. Oh and H. S. Yang, Einstein Manifolds As Yang-Mills Instantons, Mod. Phys. Lett. A 28 (2013) 1350097.
- [37] J. J. Oh, C. Park, and H. S. Yang, Yang-Mills instantons from gravitational instantons, JHEP 04 (2011) 087.
- [38] J. Lee, J. J. Oh, and H. S. Yang, An efficient representation of Euclidean gravity I, JHEP 12 (2011) 025.
- [39] H. S. Yang, Riemannian manifolds and gauge theory, Proc. Sci., CORFU2011 (2011) 063.
- [40] J. Park, J. Shin and H. S. Yang, Anatomy of Einstein manifolds, Phys. Rev. D 105 (2022) 064015.
- [41] S. K. Donaldson and P. B. Kronheimer, *The Geometry of Four-Manifolds*, Oxford Univ. Press, Oxford (1990).
- [42] M. F. Atiyah, N. Hitchin and I. M. Singer, Self-duality in four-dimensional Riemannian geometry, Proc. Roy. Soc. London A 362 (1978) 425.
- [43] A. L. Besse, *Einstein Manifolds*, Springer-Verlag, Berlin (1987).
- [44] T. Eguchi, P. B. Gilkey and A. J. Hanson, Gravitation, gauge theories and differential geometry, Phys. Rep. 66 (1980) 213.
- [45] H. A. Buchdahl, On rotor calculus I, J. Aust. Math. Soc. 6 (1966) 402.
- [46] H. A. Buchdahl, On rotor calculus II, J. Aust. Math. Soc. 6 (1966) 424.
- [47] M. Cahen, R. Debever and L. Defrise, A Complex Vectorial Formalism in Gneral Relavity, J. Math. Mech. 16 (1967) 761.

- [48] R. Portugal, Algorithmic simplification of tensor expressions, J. Phys. A: Math. Gen. 32 (1999) 7779.
- [49] D. Xu, Two important invariant identities, Phys. Rev. D 35 (1987) 769.
- [50] A. Harvey, Identities of the scalars of the four-dimensional Riemannian manifold, J. Math. Phys. 36 (1995) 356.
- [51] R. Rajaraman, *Solitons and Instantons*, North-Holland, Amsterdam, (1982).
- [52] G. 't Hooft and M. Veltman, One-loop divergencies in the theory of gravitation, Ann. Inst. H. Poincar´e Phys. Theor. A 20 (1974) 69.
- [53] G. W. Gibbons and S. W. Hawking, Classification of gravitational instanton symmetries, Commun. Math. Phys. 66 (1979) 291.
- [54] S. B. Edgar and A. H ¨oglund, Dimensionally dependent tensor identities by double antisymmetrization, J. Math. Phys. 43 (2002) 659.
- [55] G. E. Sneddon, The identities of the algebraic invariants of the four-dimensional Riemann tensor. II, J. Math. Phys. 39 (1998) 1659.
- [56] G. E. Sneddon, The identities of the algebraic invariants of the four-dimensional Riemann tensor. III, J. Math. Phys. 40 (1999) 5905.
- [57] E. Zakhary and J. Carminati, On the problem of algebraic completeness for the invariants of the Riemann tensor: I, J. Math. Phys. 42 (2001) 1474.
- [58] J. Carminati, E. Zakhary and R. G. McLenaghan, On the problem of algebraic completeness for the invariants of the Riemann tensor: II, J. Math. Phys. 43 (2002) 1474.
- [59] J. Carminati and E. Zakhary, On the problem of algebraic completeness for the invariants of the Riemann tensor: III, J. Math. Phys. 43 (2002) 4020.
- [60] I. Jack and L. Parker, Linear independence of renormalization counterterms in curved space-times of arbitrary dimensionality, J. Math. Phys. 28 (1987) 1137.
- [61] H. S. Yang and S. Yun, Calabi-Yau Manifolds, Hermitian Yang-Mills Instantons and Mirror Symmetry, Adv. High Energy Phys. 2017 (2017) 7962426 [arXiv:1107.2095].

