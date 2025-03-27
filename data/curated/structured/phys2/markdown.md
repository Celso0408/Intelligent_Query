![](_page_0_Picture_0.png)

| Title            |||| Spectral properties of a Dirac operator in the chiral quark soliton model |
| ---              |||| ---                                                                       |
| Author(s)        |||| Arai, Asao; Hayashi, Kunimitsu; Sasaki, Itaru                             |
| Citation         |||| JOURNAL OF MATHEMATICAL PHYSICS, 46, 052306                               |
|                  |||| https://doi.org/10.1063/1.1896388                                         |
| Issue Date       |||| 2005-05                                                                   |
| Doc URL          |||| http://hdl.handle.net/2115/5908                                           |
| Rights           |||| Copyright © 2005 American Institute of Physics                            |
| Type             |||| article                                                                   |
| File Information |||| JMP46-5.pdf                                                               |



![](_page_0_Picture_2.png)

JOURNAL OF MATHEMATICAL PHYSICS 46, 052306 s2005d

# **Spectral properties of a Dirac operator in the chiral quark soliton model**

Asao Arai,a! Kunimitsu Hayashi, and Itaru Sasaki *Department of Mathematics, Hokkaido University, Sapporo 060-0810, Japan*

sReceived 16 December 2004; accepted 1 March 2005; published online 20 April 2005d

We consider a Dirac operator H acting in the Hilbert space L2 sR3 ;C4 d ^ C2 , which describes a Hamiltonian of the chiral quark soliton model in nuclear physics. The mass term of H is a matrix-valued function formed out of a function F:R3→R, called a profile function, and a vector field n on R3 , which fixes pointwise a direction in the isospin space of the pion. We first show that, under suitable conditions, H may be regarded as a generator of a supersymmetry. In this case, the spectra of H are symmetric with respect to the origin of R. We then identify the essential spectrum of H under some condition for F. For a class of profile functions F, we derive an upper bound for the number of discrete eigenvalues of H. Under suitable conditions, we show the existence of a positive energy ground state or a negative energy ground state for a family of scaled deformations of H. A symmetry reduction of H is also discussed. Finally a unitary transformation of H is given, which may have a physical interpretation. © *2005 American Institute of Physics.* fDOI: 10.1063/1.1896388g

## **I. INTRODUCTION**

Let sjsj=1,2,3d be the Pauli matrices,

$$\sigma_{1}{=}\begin{pmatrix}0&1\\ 1&0\end{pmatrix},\quad\sigma_{2}{=}\begin{pmatrix}0&-i\\ i&0\end{pmatrix},\quad\sigma_{3}{=}\begin{pmatrix}1&0\\ 0&-1\end{pmatrix}\tag{1.1}$$

and

$$\alpha_{j}{=}\begin{pmatrix}\sigma_{j}&0_{2}\\ 0_{2}&-\sigma_{j}\end{pmatrix}\quad(j=1,2,3),\quad\beta{=}\begin{pmatrix}0_{2}&1_{2}\\ 1_{2}&0_{2}\end{pmatrix},\tag{1.2}$$

where 02 and 12 are the 232 zero matrix and the 232 identity matrix, respectively. The matrix

$\gamma_{5}$:= - $i\alpha_{1}\alpha_{2}\alpha_{3}$ (1.3)

is Hermitian with g5 2=14 sthe 434 identity matrixd satisfying the following relations:

$$[\alpha_{j},\gamma_{5}]=0\ (j=1,2,3),\ \ \ \{\beta,\gamma_{5}\}=0,\tag{1.4}$$

where fA,Bgª*AB−BA* and hA,Bjª*AB+BA*. We set

$$\sigma:=(\sigma_{1},\sigma_{2},\sigma_{3}),\quad\alpha:=(\alpha_{1},\alpha_{2},\alpha_{3}).\tag{1.5}$$

For objects A=sA1 ,A2 ,A3d and B=sB1 ,B2 ,B3d such that the products *AjBj* sj=1,2,3d and their sum are defined, we write A·Bªoj=1 3 *AjBj*.

We consider a Dirac operator acting in the Hilbert space

0022-2488/2005/46~5!/052306/12/$22.50 © 2005 American Institute of Physics 46, 052306-1

ad Author to whom correspondence should be addressed. Electronic mail: arai@math.sci.hokudai.ac.jp

052306-2 Arai, Hayashi, and Sasaki J. Math. Phys. 46, 052306 ~2005!

${\cal H}$:=$L^{2}({\mathbb{R}}^{3};{\mathbb{C}}^{4})\otimes{\mathbb{C}}^{2}$, (1.6)

where L2 sR3 ;C4 d is the Hilbert space of C4 -valued square integrable functions on R3 . Let ¹ªsD1 ,D2 ,D3d with Dj the generalized partial differential operator in the variable xj, the jth component of x=sx1 ,x2 ,x3d[R3 . Then the free Dirac operator with mass zero is defined by

$H_{0}$:= - $i\alpha\cdot\nabla\otimes1_{2}$ (1.7)

acting in H. To introduce a perturbation to H0, let F:R3→R be Borel measurable and finite almost everywhere sa.e.d in R3 and set

$U_{F}$:=$\cos F+i\gamma_{5}\otimes\tau\cdot{\bf n}\,\sin F$, (1.8)

where tªst1 ,t2 ,t3d with t jªsjsj=1,2,3d, nªsn1 ,n2 ,n3d with nj a real-valued measurable function on R3 such that

$\mathbf{n(x)}|^{2}=1,\quad\text{a.e.}\mathbf{x}\in\mathbb{R}^{3}.$

Let M .0 be a constant. Then, by the second relation in s1.4d, Msb ^ 12dUF is a bounded selfadjoint operator on H. Hence, by the Kato–Rellich theorem, the operator

$H$:=$H_{0}+M(\beta\otimes1_{2})U_{F}$ (1.10)

is self-adjoint with domain DsHd=DsH0d. This is the Dirac operator we consider in this paper. The operator H appears as the Hamiltonian of the so-called the chiral quark soliton model in nuclear physics se.g., Ref. 1 and references thereind. In this context, M and

$\Phi_{F}$:=$\cos F+i\sin F\otimes\tau\cdot\mathbf{n}$ (1.11)

sUF with g5 replaced by 14d denote the mass of a quark and the pion field, respectively, and F is called a profile function. The Dirac operator H is not only physically important, but also may have interests from purely mathematical points of view. As far as we know, no mathematically rigorous analysis has been made on the Dirac operator H sa study of a Dirac operator with a variable mass is given in Ref. 2, but, in that paper, the mass is a scalar function and the point there is to establish self-adjointness of such a Dirac opeartor in cases where the Kato–Rellich theorem is no longer applicable to it; in this sense Ref. 2 does not bear upon the topics of the present paperd.

The present paper is organized as follows. In Sec. II, we show that the Dirac operator H can be regarded as a generator of a supersymmetry, and describe its implications on the spectra of H. In Sec. III we identify the essential spectrum of H. We also derive an upper bound for the number of discrete eigenvalues of H. In particular, for a class of F and n, the absence of discrete eigenvalues of H is proven. Sections IV and V are concerned with existence of discrete eigenvalues of H. In Sec. IV we introduce a concept of a positive energy ground state and that of a negative energy ground state of H and show, under some condition for F, that a scaled deformation of H has a positive energy ground state or a negative ground state. In Sec. V we discuss a symmetry reduction of H to smaller mutually orthogonal closed subspaces which are indexed by triples s,,s,td[Z3h±1j3h±1j, where , denote an eigenvalue of the third component of the angular momentum operator, s/2 the spin of the quark and t/2 the isospin of the pion. We prove that, under suitable conditions, each reduced part of H or its scaled version has a discrete positive ground state or a discrete negative ground state. In the last section we present a unitary transformation which brings H to a Dirac operator with a magnetic moment.

#### **II. SUPERSYMMETRIC ASPECTS**

In this section we assume the following. *Hypothesis (I):* Each njsj=1,2,3d is continuously differentiable on R3 and

$(n_{1}({\bf x}),n_{2}({\bf x}))\neq(0,0),\quad{\bf x}\in\mathbb{R}^{3}$.

Let

$$\xi(\mathbf{x}):=\frac{(\tau_{1}n_{2}(\mathbf{x})-\tau_{2}n_{1}(\mathbf{x}))}{\sqrt{n_{1}(\mathbf{x})^{2}+n_{2}(\mathbf{x})^{2}}},\quad\mathbf{x}\in\mathbb{R}^{3}.\tag{2.2}$$

Then jsxd 2=1, x[R3 . For all x[R3 , we can define a matrix tensor

$\Gamma({\bf x})$:=$\alpha_{1}\alpha_{2}\alpha_{3}\beta\otimes\xi({\bf x})$ (2.3)

acting on C4 ^ C2 . It is easy to see that Gsxd is self-adjoint with Gsxd 2=I sI denotes identityd. By the natural identification H=L2 sR3 ;C4 ^ C2 d, we denote the multiplication operator by the matrixtensor valued function Gs·d by the same symbol G. Then G is self-adjoint and unitary on H.

*Proposition 2.1: Suppose that Hypothesis (I) holds and* jsxd *is a constant matrix. Then, for all* c[DsHd, Gc[DsHd and

$\{\Gamma,H\}\psi=0,\quad\psi\in D(H)$.

*Proof:* By direct computations, we have

$$\{\alpha_{1}\alpha_{2}\alpha_{3}\beta,\alpha_{j}\}=0\quad(j=1,2,3),\quad\{\xi({\bf x}),\tau\cdot{\bf n}({\bf x})\}=0.\tag{2.5}$$

Using these relations and the constancy of js·d, we see that, for all c[DsHd=DsH0d, Gc[DsH0d and H0Gc=−GH0c. Similarly, using s2.5d and fa1a2a3b,bg5g=0, we see that hMsb ^ 12dUF,Gjc=0. Thus s2.4d follows. j

Proposition 2.1 shows that the Dirac operator H may be regarded as a generator of a supersymmetry, i.e., a supercharge with respect to G se.g., p. 140 in Ref. 3d.

For a self-adjoint operator T, we denote by ssTd frespectively, spsTdg the spectrum of T srespectively, the point spectrum of Td. The discrete spectrum of T sthe set of isolated eigenvalues of T with finite multiplicityd is denoted sdsTd.

**Theorem 2.2:** *Suppose that Hypothesis (I) holds and* jsxd *is a constant matrix. Then*

- sid ssHd *is symmetric with respect to the origin of* R, *i.e., if* l[ssHd, *then* −l[ssHd.
- siid s#sHds#=p,dd *is symmetric with respect to the origin of* R. *The multiplicity* l[s#sHd *coincides with that of* −l[s#sHd.

*Proof:* By Proposition 2.1 we have GHG−1=−H sthe unitary equivalence of H and −Hd. This implies the desired results. j

*Remark 2.1:* The properties stated in Theorem 2.2 may differ from spectral properties of the usual Dirac operator H0+Mb+V, where V is a scalar potential.

### **III. THE ESSENTIAL SPECTRUM AND FINITENESS OF THE DISCRETE SPECTRUM** OF H

#### **A. Structure of the spectrum of** H

For a self-adjoint operator T, we denote by sesssTd the essential spectrum of T. **Theorem 3.1:** *Suppose that*

$\lim\;F({\bf x})=0$.

$|{\bf x}|\rightarrow\infty$

*Then*

$$\sigma_{\rm ess}(H)=(-\,\infty,-\,M]\cup[M,\infty),\tag{3.2}$$

$\sigma_{\rm d}(H)\subset(-M,M)$.

*Proof:* We write H=H0+Msb ^ I2d+V with VªMsb ^ I2dsUF−Id. We have iVsxdiøMsu1 −cos Fsxdu+usin Fsxdud→0suxu→`d. Hence we can apply Theorem 4.7, Remark 2 on p. 117 in Ref. 052306-4 Arai, Hayashi, and Sasaki J. Math. Phys. 46, 052306 ~2005!

3 to H to obtain s3.2d. This implies s3.3d. j

#### **B. Bound for the number of discrete eigenvalues of** H

Assume s3.1d. Then, by Theorem 3.1, we can define the number of discrete eigenvalues of H counting multiplicities,

$N_{H^{\dagger}}$=dim Ran $E_{H}((-M,M))$, (3.4)

where EH is the spectral measure of H and Ran EHss−M ,Mdd means the range of EHss−M ,Mdd. To estimate an upper bound for NH, we introduce a hypothesis for F and n.

*Hypothesis (II):*

- sid The functions F and nj sj=1,2,3d are continuously differentiable on R3 .
- siid The functions DjF and *Djnk* sj,k=1,2,3d are bounded on R3 .

Under this assumption, we can define

$$V_{F}({\bf x})\!:=\sqrt{\left|\ \nabla\,F({\bf x})\right|^{2}+\sum_{k=1}^{3}\left|\ \nabla\,n_{k}({\bf x})\right|^{2}\sin^{2}F({\bf x})},\quad{\bf x}\in\mathbb{R}^{3}.\tag{3.5}$$

**Theorem 3.2:** *Assume (3.1) and Hypothesis (II). Suppose that*

$$C_{F^{2}}{=}\int_{\mathbb{R}^{6}}\frac{V_{F}({\bf x})V_{F}({\bf y})}{|{\bf x}-{\bf y}|^{2}}{\rm d}{\bf x}\;{\rm d}{\bf y}<\infty.\tag{3.6}$$

*Then NH is finite with*

$$N_{H}\leq\frac{M^{2}C_{F}}{2\pi^{2}}.\tag{3.7}$$

To prove this theorem we present a general lemma. Let K be a complex Hilbert space and BsKd be the Banach space of bounded linear operators on K. Let V:Rd→BsKd sd[Nd be a measurable function. The function V defines a unique multiplication operator acting in the Hilbert space L2 sRd ;Kd of K-valued square integrable functions on Rd . We denote it by the same symbol V. We assume the following sD is the d-dimensional generalized Laplaciand:

sV.1d Dss−Dd 1/2d,DsuVu 1/2dùDsuV* u 1/2d and the form sum

$$L_{0}{:=-\,\Delta\,+\,}\left(\begin{array}{c c}{{-\,|V|}}&{{0}}\\ {{0}}&{{-\,|V^{*}|}}\end{array}\right)$$

acting in %2 L2 sRd ;Kd with form domain Dss−Dd 1/2d defines a unique self-adjoint operator bounded from below. Moreover, sesssL0d,f0,`d.

sV.2d The operator

$$L{\mathrel{\vbox{\hbox{\scriptsize.}\mkern-14mu=}}}-\Delta+\begin{pmatrix}0&V^{*}\\ V&0\end{pmatrix}$$

acting in %2 L2 sRd ;Kd is self-adjoint on DsDd, bounded from below, and sesssLd,f0,`d.

For a self-adjoint operator A, we denote by N−sAd the number of negative eigenvalues of A counting multiplicities.

*Lemma 3.3: Assume (V.1) and (V.2). Then N−*sLdøN−sL0d. *Proof:* Let

**Downloaded 19 Mar 2006 to 133.87.26.100. Redistribution subject to AIP license or copyright, see http://jmp.aip.org/jmp/copyright.jsp**

052306-5 Dirac operator in the chiral quark soliton model J. Math. Phys. 46, 052306 ~2005!

$$Q{\mathrm{:=}}{\binom{0}{V}}.$$

Then Q is self-adjoint and

$$Q^{2}=\left(\begin{array}{l l}{{|V|^{2}}}&{{0}}\\ {{0}}&{{|V^{*}|^{2}}}\end{array}\right),$$

which implies that

$$|Q|={\binom{|V|}{0}}\quad0\quad.$$

It is obvious that Qù−uQu. Hence LùL0. This inequality and the min–max principle se.g., Theorem XIII.1, Problem 1 in Ref. 4d imply the inequality N−sLdøN−sL0d. j

*Proof of Theorem 3.2:* We note that H has the operator matrix representation

$$H=H_{0}+M\Biggl{(}\begin{array}{cc}0&\Phi_{F}^{*}\\ \Phi_{F}&0\end{array}\Biggr{)},\tag{3.8}$$

where FF is defined by s1.11d. Hence

$$H^{2}=L(F)+M^{2}\tag{3.9}$$

with

$$L(F):=-\,\Delta+M\!\left(\begin{array}{cc}0&W_{F}^{*}\\ W_{F}&0\end{array}\right),\tag{3.10}$$

where WFªis·s¹FFd. Note that, by Hypothesis sIId siid, the second term on the right-hand side of s3.10d is a bounded self-adjoint operator and hence LsFd is self-adjoint with DsLsFdd=DsDd. By direct computations, we have

$W_{F}({\bf x})^{*}W_{F}({\bf x})=W_{F}({\bf x})W_{F}({\bf x})^{*}=|\ \nabla\ F({\bf x})|^{2}+\sum_{j=1}^{3}|\ \nabla\ n_{j}({\bf x})|^{2}\ \sin^{2}F({\bf x}),$

where we have used s1.9d. Hence uWFu=uWF * u=VF. Let L0sFdª−D*−MVF*. By Theorem 3.1, sesssLsFdd=f0,`d. Condition s3.6d implies that VF is a potential in the Rollnik class sp. 170 in Ref. 5d. Hence it follows from Example 7, p. 118 in Ref. 4 and Weyl's essential spectrum theorem sTheorem XIII.14, p. 112 in Ref. 4d that sesssL0sFdd=sesss−Dd=f0,`d. Therefore the assumption of Lemma 3.3 with L=LsFd and *L0=L0*sFd is satisfied. Hence N−sLsFddøN−sL0sFdd. It is well known that N−sL0sFddø8M2 CF/s4pd 2 sTheorem XIII.10 in Ref. 4d, where the factor 8=dim C4 ^ C2 . On the other hand, by the spectral theorem, NHøN−sLFd. Thus s3.7d follows. j

Theorem 3.2 implies the absence of discrete eigenvalues of H for F's such that the Rollnik norm of MVF is sufficiently small.

*Corollary 3.4: Assume (3.1) and Hypothesis (II). Let M2* CF,2p2 . *Then* sdsHd=0".

## **IV. EXISTENCE OF DISCRETE GROUND STATES**

For a self-adjoint operator A bounded from below, we set

E0sAdªinf ssAd.

If E0sAd[spsAd, then we say that A has a ground state and we call a nonzero vector in kersA −E0sAdd a ground state of A. If E0sAd[sdsAd, then we say that A has a discrete ground state.

*Definition 4.1:* Let

052306-6 Arai, Hayashi, and Sasaki J. Math. Phys. 46, 052306 ~2005!

$$E_{0}^{+}(H)\!:=\inf(\sigma(H)\cap[0,\infty)),\quad E_{0}^{-}(H)\!:=\sup(\sigma(H)\cap(-\infty,0]).\tag{4.1}$$

If E0 + sHd frespectively, E0 − sHdg is an eigenvalue of H, then we say that H has a positive srespectively, negatived energy ground state and we call a nonzero vector in kersH−E0 + sHdd frespectively, kersH−E0 − sHddg a positive srespectively, negatived energy ground state of H. If E0 + sHd frespectively, E0 − sHdg is a discrete eigenvalue of H, then we say that H has a discrete positive srespectively, negatived energy ground state.

*Remark 4.1:* If the spectrum of H is symmetric with respect to the origin of R as in Theorem 2.2, then E0 + sHd=−E0 − sHd, and H has a positive energy ground state if and only if it has a negative energy ground state.

We assume Hypothesis sIId. Then the operators

$$S_{\pm}(F):=-\,\Delta\pm M(D_{3}\,\cos F)=-\,\Delta\mp M(D_{3}F)\sin F\tag{4.2}$$

are self-adjoint with DsS±sFdd=DsDd and bounded from below.

*Theorem 4.2: Assume Hypothesis (II) and (3.1). Suppose that E0*sS+sFdd,0 or E0sS−sFdd ,0. *Then H has a discrete positive energy ground state or a discrete negative ground state.*

*Proof:* For each f [DsDd and u[C2 with iui=1, we define

$$\psi_{f}^{+}{:=}(f\otimes u,0,i f\otimes u,0)\in{\mathcal{H}},\quad\psi_{f}{:=}(0,f\otimes u,0,i f\otimes u)\in{\mathcal{H}}.$$

Then we have

$$\langle\psi_{f}^{\pm},L(F)\psi_{f}^{\pm}\rangle=2\langle f,S_{\pm}(F)f\rangle.$$

In the case where E0sS+sFdd,0, there exists a unit vector f [DsDd such that kf ,S+sFdfl,0. Hence kcf + ,LsFdcf + l,0. By Theorem 3.1 and the spectral theorem, we have

$\sigma_{\rm ess}(L(F))=[0,\infty)$.

Thus, by the min–max principle, LsFd has a discrete ground state. Similarly, in the case where E0sS−sFdd,0 too, LsFd has a discrete ground state. This implies that H has a discrete positive energy ground state or a discrete negative ground state. j

To construct examples of F satisfying the conditions as stated in Theorem 4.2, we consider a scaling. For a constant «.0 and a function f on Rd , we define a function f« on Rd by

$$f_{x}(x){:=}f(e x),\quad x\in\mathbb{R}^{d}.$$

*Lemma 4.3: Let V*:Rd→R *be in L*loc 2 sRd d *and, for a constant* «.0,

$$S_{e}\!:=-\,\Delta+V_{e}.$$

*Suppose that the following conditions are satisfied:*

- sid *For all* «.0, S« *is self-adjoint and bounded from below and* sesssS«d,f0,`d.
- siid *There exists a nonempty open set* V,hx[Rd uVsxd,0j.

*Then there exists a constant* «0.0 *such that, for all* «[s0,«0d, S« *has a discrete ground state.*

*Proof:* By condition siid, we can take a nonzero vector f [C0 `sVd sthe set of infinitely differentiable functions on Rd with compact support in Vd. Then it is easy to see that kf« ,S«f«l =«−d saf«2−ubfud, where afªi¹ fi 2 , bf =kf ,Vfl,0. Hence, taking «0ªÎubfu/af snote that af Þ0d, we have kf« ,S«f«l,0 for all «[s0,«0d. Hence, by the min–max principle and condition sid, E0sS«d[sdsS«d. j

*Lemma 4.4: Let V:*Rd→R *be continuous on* Rd *with* limuxu→` Vsxd=0. *Suppose that* V−ªhx[Rd uVsxd,0jÞ0". *Then the following hold:*

- sid −D+*V acting in L2* sRd d *is self-adjoint and bounded from below.*
- siid sesss−D+Vd=f0,`d.

- siiid S« *has a discrete ground state for all* «[s0,«0d *with some* «0.0.
*Proof:* Part sid follows from the Kato–Rellich theorem. Part siid is proven by a simple application of Theorem XIII.15-sbd in Ref. 4.

Since V is continuous, the set V− is open. Hence Lemma 4.3 implies the existence of a ground state of S« for all «[s0,«0d with some «0.0. j

We consider a one-parameter family of Dirac operators,

$$H_{\varepsilon}:=H_{0}+\frac{1}{\varepsilon}M(\beta\otimes1_{2})U_{F_{\varepsilon}},\tag{4.4}$$

which is a scaled deformation of H.

*Theorem 4.5: Assume Hypothesis (II) and (3.1). Suppose that D*3 cos *F is not identically zero. Then there exists a constant* «0.0 *such that, for all* «[s0,«0d, H« *has a discrete positive energy ground state or a discrete negative ground state.*

*Proof:* We write S±sF,MdªS±sFd to make explicit the dependence of S±sFd on M. At least one of the sets hx[R3 u sD3 cos Fdsxd.0j and hx[R3 sD3 cos Fdsxd,0j is not empty. The function D3 cos F=−sD3Fdsin F is bounded and continuous satisfying limuxu→`sD3Fdsxd=0. Hence we can apply Lemma 4.4 to conclude that S+sF« ,«−1Md or S−sF« ,«−1Md has a discrete ground state for all «[s0,«0d with some «0.0. This fact and Theorem 4.2 yield the desired result. j

#### **V. SYMMETRY REDUCTION OF** H

In this section, we show that, if F is invariant under the rotations around the x3 axis, then there exist infinitely many mutually orthogonal closed subspaces of H that reduce H« for all «.0 and each reduced part of H« may have a positive energy ground state or a negative energy ground state. We use the cylindrical coordinates for points x=sx1 ,x2 ,x3d[R3 ,

$$x_{1}=r\cos\,\theta,\quad x_{2}=r\sin\,\theta,\quad x_{3}=z,$$

where u[f0,2pd, r.0. We assume the following.

*Hypothesis (III):* There exists a continuously differentiable function G:s0,`d3R→R such that sid Fsxd=Gsr,zd, x[R3 \h0j; siid limr+uzu→` Gsr,zd=0; siiid supr.0,z[Rsu]Gsr,zd/]ru +u]Gsr,zd/]zud,`.

We take the vector field n to be of the form

$\mathbf{n(x)}$:=$(\sin\Theta(r,z)\cos(m\theta),\sin\Theta(r,z)\sin(m\theta),\cos\Theta(r,z))$, (5.1)

where Q:s0,`d3R→R is continuous and m is a real constant.

Let L3ª*−ix1D2+ix2D*1, the third component of the angular momentum. It is well known that L3 is essentially self-adjoint on C0 `sR3 d. We denote its closure by the same symbol L3. We set

$$\Sigma_{3}{:=}\sigma_{3}\oplus\sigma_{3}$$

acting on C4 and define

$$K_{3^{1}}{=}L_{3}\otimes1_{2}+\frac{1}{2}\Sigma_{3}\otimes1_{2}+\frac{m}{2}I\otimes\tau_{3},\tag{5.2}$$

which is a self-adjoint operator acting in H.

We denote by T« s«.0d the unitary dilation on L2 sR3 d with power «,

$(T_{\varepsilon}f)({\bf x})$:=$\varepsilon^{3/2}f(\varepsilon{\bf x}),\quad f\in L^{2}({\mathbb{R}}^{3}),\ {\rm a.e.}\ {\bf x}.$ (5.3)

*Lemma 5.1: For all* «.0, T«L3T« −1=L3. *Hence* sT« ^ 12dK3sT« ^ 12d −1=K3 *for all* «.0.

*Proof:* It is straightforward to see that, for all f [C0 `sR3 d, T«L3f =L3T«f. Since C0 `sR3 d is a core of L3, this equality extends to all f [DsL3d showing that L3,T« −1L3T«. The both sides are 052306-8 Arai, Hayashi, and Sasaki J. Math. Phys. 46, 052306 ~2005!

self-adjoint. Hence they coincide. j

*Lemma 5.2: Assume that*

Qs«r,«zd = Qsr,zd, sr,zd [ s0,`d 3 R, « . 0. s5.4d

*Then, for all t*[R and «.0, *the operator equality*

$$e^{itK_{3}}H_{e}e^{-itK_{3}}=H_{e}\tag{5.5}$$

*holds.*

*Proof:* We first prove s5.5d with «=1. We have for all t[R,

$$e^{i t K_{3}}=e^{i t L_{3}}e^{i t\Sigma_{3}/2}\otimes e^{i t m\tau_{3}/2}.$$

For all f [C0 `sR3 d, we have

$(e^{itL_{3}}f)({\bf x})=f(x_{1}\cos t-x_{2}\sin t,x_{1}\sin t+x_{2}\cos t,z),\quad{\bf x}\in\mathbb{R}^{3}$.

Hence *eitL*3 leaves C0 `sR3 d invariant. It follows that, for all f [C0 `sR3 ;C4 d ^ C2 , eitK3f [DsH0d =DsHd and

$$H_{0}e^{i\mu L_{2}}f=e^{i\mu L_{2}}\{(-i\alpha_{1}\cos t+i\alpha_{2}\sin t)D_{1}f+(-i\alpha_{1}\sin t-i\alpha_{2}\cos t)D_{2}f-i\alpha_{3}D_{3}f\}.\tag{5.6}$$

Using the matrix representation of aj, one can check that

$$\alpha_{j}e^{i t\Sigma_{3}/2}=e^{-i t\Sigma_{3}/2}\alpha_{j}\quad(j=1,2),\quad[\alpha_{3},e^{i t\Sigma_{3}}]=0.$$

It follows from these relations and s5.6d,

$H_{0}e^{itK_{3}}f=e^{itK_{3}}H_{0}f$.

We have

$$\tau_{j}e^{i m\tau_{3}/2}=e^{i m\tau_{3}/2}\tau_{j}e^{i m\tau_{3}}\quad(j=1,2),\quad\tau_{3}e^{i m\tau_{3}/2}=e^{i m\tau_{3}/2}\tau_{3}$$

and

$e^{-itL_{3}}\mathbf{n}(\mathbf{x})e^{itL_{3}}=(\sin\Theta(r,z)\cos m(\theta-t),\sin\Theta(r,z)\sin m(\theta-t),\cos\Theta(r,z))$.

It follows from these relations that

$\beta\otimes1_{2}U_{F}e^{itK_{3}}f=e^{itK_{3}}(\beta\otimes1_{2})U_{F}f$. (5.8)

Combining s5.7d together with s5.8d, we obtain *HeitK*3f =*eitK3Hf*. Since C0 `sR3 ;C4 d ^ C2 is a core of H, this equality extends to all f [DsHd=DsH0d showing H,*e−itK3HeitK*3. The both sides are self-adjoint. Thus s5.5d follows.

We next consider the case where «Þ1. We write UF=UsF,nd. By Lemma 5.1, s5.8d and the fact that T« is a bijection from C0 `sR3 d onto itself, we have b ^ 12UsF« ,n«d*eitK3f =eitK*3sb ^ 12dUsF« ,n«df. By condition s5.4d, n«=n. Hence b ^ 12UsF« ,n«d*eitK*3f *=eitK*3sb ^ 12dUsF« ,ndf. Therefore s5.8d holds with F replaced by F«. Thus, in the same way as in the preceding paragraph, one can prove s5.5d. j

We say that two self-adjoint operators on a Hilbert space strongly commute if their spectral measures commute.

*Lemma 5.3: Assume (5.4). Then, for all* «.0, H« *and K3 strongly commute*.

*Proof:* It follows from Lemma 5.2 and the functional calculus for self-adjoint operators that *eitK3eisH*«*=eisH*«*eitK*3 for all s, t[R and all «.0. This implies the strong commutativity of H« and K3 ssee Theorem VIII.13 in Ref. 6 for general criteria of the strong commutativity of self-adjoint operatorsd. j

Let

052306-9 Dirac operator in the chiral quark soliton model J. Math. Phys. 46, 052306 ~2005!

$E$:=$(0,\infty)\times[0,2\pi)\times\mathbb{R}=\{(r,\theta,z)|r>0,\theta\in[0,2\pi),z\in\mathbb{R}\}$

and dmªr dr ^ du ^ dz, a measure on E. Then one can define a unitary operator Y :L2 sR3 d →L2 sE,dmd by

$$(Y f)(r,\theta,z):=f(r\cos\,\theta,r\,\sin\,\theta,z),\quad f\in L^{2}(\mathbb{R}^{3}).$$

For each ,[Z, we define f, :f0,2pd→C by

$$\phi_{\ell}(\theta):=\frac{1}{\sqrt{2\,\pi}}e^{i\ell\theta},\quad\theta\in[0,2\,\pi).\tag{5.9}$$

It is well known that hf,j,[Z is a complete orthonormal system of L2 sf0,2pdd. For each f [L2 sE,dmd, we define f ˆ:s0,`d3Z3R by

$$\hat{f}(r,\,\ell\,,z){:=}\int_{0}^{2\pi}\phi_{\ell}(\theta)^{*}f(r,\theta,z)\mathrm{d}\theta.$$

We define an operator Du on L2 sE,dmd as follows:

$$D(D_{\theta})\!:=\!\left\{f\!\in\!L^{2}(E,\mathrm{d}\mu)|\sum_{\ell=-\infty}^{\infty}\ell^{2}\!\int_{0}^{\infty}\mathrm{d}r\,r\!\int_{\mathbb{R}}\mathrm{d}z|\widehat{f}(r,\,\ell\,,z)|^{2}<\infty\right\},$$

$$(D_{\theta})(r,\,\ell\,,\theta)=i\,\ell\,\widehat{f}(r,\,\ell\,,\theta),\quad f\!\in\!D(D_{\theta})\,.$$

Then −iDu is self-adjoint with

$$\sigma(-iD_{\theta})=\sigma_{\rm p}(-iD_{\theta})=\{\ell\}_{\ell\in\mathbb{Z}}=\mathbb{Z},\tag{5.10}$$

$$\ker(-iD_{\theta}-\ \ell\ )=\left\{g\phi_{\ell}|g\colon(0,\infty)\times\mathbb{R}\to\mathbb{C},\int_{0}^{\infty}\mathrm{d}r\,r\int_{\mathbb{R}}\mathrm{d}z|g(r,z)|^{2}<\infty\right\}.\tag{5.11}$$

It is not so hard to see that

$Y_{L_{3}}Y^{-1}=-iD_{\theta}$.

Hence

$\sigma(L_{3})=\sigma_{\rm p}(L_{3})=\mathbb{Z}$.

Let

$${\cal M}_{\ell}:={\rm ker}(L_{3}-\ \ell\ )=Y^{-1}\ {\rm ker}(-iD_{\theta}-\ \ell\ ).\tag{5.14}$$

Then we have the orthogonal decomposition

$$L^{2}({\rm R}^{3})=\oplus^{\infty}_{\ell=-\infty}{\cal M}_{\ell},\quad L^{2}(E,{\rm d}\mu)=\oplus^{\infty}_{\ell=-\infty}YM_{\ell}.\tag{5.15}$$

By s5.13d, we have

$$\sigma(K_{3})=\sigma_{\rm p}(K_{3})=\left\{\ell+\ \frac{s}{2}+\frac{mt}{2}|\ \ell\in\mathbb{Z},s=\ \pm1,t=\ \pm1\right\}.\tag{5.16}$$

The eigenspace of K3 with eigenvalue ,+ss/2d+smt/2d is given by

**Downloaded 19 Mar 2006 to 133.87.26.100. Redistribution subject to AIP license or copyright, see http://jmp.aip.org/jmp/copyright.jsp**

052306-10 Arai, Hayashi, and Sasaki J. Math. Phys. 46, 052306 ~2005!

${\cal M}_{\ell,s,t}$:=${\cal M}_{\ell}\otimes{\cal C}_{s}\otimes{\cal T}_{t}$ (5.17)

under the natural identificaion H=L2 sR3 d ^ C4 ^ C2 , where CsªkersS3−sd and Tt ªkerst3−td. Then H has the orthogonal decomposition

$${\cal H}=\oplus_{\ell\in{\mathbb{Z}},s,t\in\{\pm1\}}{\cal M}_{\ell,s,t}.\tag{5.18}$$

Lemma 5.3 implies the following fact.

*Lemma 5.4: Assume (5.4). Then, for all* «.0, H« *is reduced by each* M,,s,t . We denote by H«s,*,s,t*d by the reduced part of H« to M,,s,t and set

$H(\ell,s,t)$:=$H_{1}(\ell,s,t)$, (5.19)

the reduced part of H to M,,s,t .

For s= ±1 and ,[Z, we define

$$S_{s}(G,\,\ell\,):=-\,\frac{\partial^{2}}{\partial r^{2}}-\frac{1}{r}\frac{\partial}{\partial r}+\frac{\ell^{2}}{r^{2}}+\frac{\partial^{2}}{\partial z^{2}}+sM\frac{\partial\mbox{cos}G}{\partial z}\tag{5.20}$$

acting in L2 ss0,`d3R,r dr dzd with domain DsSssG, ,ddªC0 `ss0,`d3Rd and set

$\mathcal{E}_{0}(S_{s}(G,\,\ell\,))$:= $\inf\limits_{f\in C_{0}^{\infty}((0,\infty)\times\mathbb{R}),\|f\|_{L^{2}((0,\infty)\times\mathbb{R},r\,dr\,dz)}=1}\langle f,S_{s}(G,\,\ell\,)f\rangle$.

**Theorem 5.5:** *Assume Hypothesis (III). Fix an* ,[Z *arbitrarily and s*= ±1. *Suppose that* E0sSssG, ,dd,0. *Then, for each t*= ±1, Hs,,s,td *has a discrete positive energy ground state or a discrete negative ground state.*

*Proof:* Let

$$c_{\ell}:=\frac{1}{\sqrt{2\,\pi}}\int_{0}^{2\pi}\mathrm{d}\theta e^{-i\ell\,\theta}\cos(m\theta),\quad\mathrm{d}_{\ell}:=\frac{1}{\sqrt{2\,\pi}}\int_{0}^{2\pi}\mathrm{d}\theta e^{-i\ell\,\theta}\sin(m\theta)\,,$$

$$n_{j,\ell}(r,z):=(\sin\Theta(r,z)c_{\ell},\sin\Theta(r,z)d_{\ell},\cos\Theta(r,z)),$$

$\Phi_{G,\ell,i}$:=cos $G+i\sum_{j=1}n_{j,\ell}$ sin $G\otimes\tau_{j}+im_{3,\ell}$ sin $G$,

$$D_{1,\ell}:=c_{\ell}\frac{\partial}{\partial r}-\frac{d_{\ell}}{r}\frac{\partial}{\partial\theta},\quad D_{2,\ell}:=d_{\ell}\frac{\partial}{\partial r}+\frac{c_{\ell}}{r}\frac{\partial}{\partial\theta}$$

and

$$W_{G_{\varepsilon},\ell,s,t}:=i\sum_{j=1}^{2}\,\sigma_{j}D_{j,\ell}\Phi_{G_{\varepsilon},\ell,t}+i s D_{z}\Phi_{G_{\varepsilon},\ell,t},\quad\varepsilon>0.$$

Then we have

$(Y\otimes1_{2})H_{\varepsilon}(\ell,s,t)^{2}(Y\otimes1_{2})^{-1}=-\frac{\partial^{2}}{\partial r^{2}}-\frac{1}{r}\frac{\partial}{\partial r}+\frac{\ell^{2}}{r^{2}}+\frac{\partial^{2}}{\partial z^{2}}+\varepsilon^{-1}M\!\left(\begin{array}{cc}0&W^{s}_{G_{\varepsilon},\ell,s,t}\\ W_{G_{\varepsilon},\ell,s,t}\end{array}\right)+M^{2}$

$$=:L_{e}(\ell,s,t)+M^{2}$$

on C0 `ss0,`d3Rd.

For each f [C0 `ss0,`d3Rd and ut[C2 satisfying ifi=1, iut i=1, and t3ut=tut st=±1d, we define

**Downloaded 19 Mar 2006 to 133.87.26.100. Redistribution subject to AIP license or copyright, see http://jmp.aip.org/jmp/copyright.jsp**

$$u_{f}^{(1)}:=(f\otimes u_{t},0,i f\otimes u_{t},0)\in{\mathcal{M}}(\ell,1,t),$$

$$\psi_{f}^{(-1)}{=}(0,f\otimes u_{t},0,i f\otimes u_{t})\in{\mathcal{M}}(\ell,-1,t).$$

Then we have

$$\langle\psi_{f}^{(s)},Y L_{1}(\ell,s,t)Y^{-1}\psi_{f}^{(s)}\rangle=2\langle f,S_{s}(F,\,\ell\,)f\rangle.$$

By the present assumption, there exists a unit vector f [C0 `ss0,`d3Rd such that kf ,SssF, ,dfl ,0. Note that sesssL1s,,s,tdd,f0,`d. Hence, by the min–max principle, L1s,*,s,t*d has a discrete ground state. This implies that Hs,,s,td has a discrete positive energy ground state or a discrete negative ground state. j

**Theorem 5.6:** *Assume Hypothesis (III) and (5.4). Suppose that* ] cos G/]*z is not identically zero. Then, for each* ,[Z, *there exists a constant* «,.0 *such that, for all* «[s0,«,d, *each* H«s,,s,td *has a discrete positive energy ground state or a discrete negative ground state.*

*Proof:* We write *Ss,M*sF, ,dªSssF, ,d to make explicit the dependence of SssF, ,d on M. In the same way as in the proof of Theorem 4.5, one can take a vector f«[C0 `ss0,`d3Rd such that kf« ,Ss,«−1MsF«s,ddf«l,0 for all sufficiently small «.0, where the smallness depends on ,. It follows from the proof of the preceding theorem that L«s,,s,td has a discrete ground state. j

*Corollary 5.7: Assume Hypothesis (III) and (5.4). Suppose that* ] cos G/]*z is not identically zero. Let* «, *be as in Theorem 5.6 and, for each N*[N *and k*.n sk,n[Zd, nk,nªminn+1ø,øk «,. *Then, for each* «[s0,nk,nd, H« *has at least* sk−nd *discrete eigenvalues counting multiplicities*.

*Proof:* We have spsH«d=ø,[Z,s,t=±1spsH«s,,s,tdd. By the preceding theorem, for each ,=n +1,…,k, H«s,,s,td has a discrete eigenvalue. Thus the desired result follows. j

*Remark 5.1:* This result is consistent with Theorem 3.2, because it reads in the present case

$$N_{H_{e}}\leq\frac{1}{\varepsilon^{4}}\frac{M^{2}C_{F}}{2\pi^{2}}$$

and the right-hand side diverges as «→0.

## **VI. A UNITARY TRANSFORMATION**

In this section we show that, under Hypothesis sIId, the Hamiltonian H with n constant is unitarily equivalent to an operator which resembles a Dirac operator with a magnetic moment.

It is easy to see that the operator

$$X_{F^{2}}{=}\begin{pmatrix}e^{iF\otimes\tau\mathbf{n}/2}&0\\ 0&e^{-iF\otimes\tau\mathbf{n}/2}\end{pmatrix}\tag{6.1}$$

is unitary. Under Hypothesis sIId, we can define the following functions:

$$B_{j}({\bf x}):=\frac{1}{2}D_{j}(F({\bf x})\otimes\tau\cdot{\bf n}({\bf x})),\quad{\bf x}\in\mathbb{R}^{3},\,j=1,2,3.\tag{6.2}$$

We set

B:=($B_{1}$,$B_{2}$,$B_{3}$)

and introduce

$H({\bf B})$:=$H_{0}+M\beta-\sigma\cdot{\bf B}$ (6.4)

acting in H. Note that, under Hypothesis sIId, the operator −s·B is a bounded self-adjoint operator. Hence, by a simple application of the Kato–Rellich theorem, HsBd is self-adjoint with DsHsBdd=DsH0d.

*Proposition 6.1: Assume Hypothesis (II) and that* n *is constant. Then*

052306-12 Arai, Hayashi, and Sasaki J. Math. Phys. 46, 052306 ~2005!

$X_{F}HX_{F}^{-1}=H({\bf B})$.

*Proof:* Noting the fact that st·nd 2=12, we have

$$\Phi_{F}=e^{i F\otimes\tau\mathbf{n}}.$$

It follows from this fact and s3.8d that *XFHXF* −1c=HsBdc for all c[f%4 C0 `sR3 dg ^ C2 . Since f%4 C0 `sR3 dg ^ C2 is a core of HsBd, the operator equality s6.5d follows. j

#### **ACKNOWLEDGMENT**

The authors thank Dr. T. Miyao for discussions.

1 N. Sawado, Phys. Lett. B 524, 289 s2002d. 2 H. Kalf and O. Yamada, J. Math. Phys. 42, 2667 s2001d.

3 B. Thaller, *The Dirac Equation* sSpringer, Berlin, Heidelberg, 1992d. 4 M. Reed and B. Simon, *Methods of Modern Mathematical Physics IV: Analysis of Operators* sAcademic, New York, 1978d. 5 M. Reed and B. Simon, *Methods of Modern Mathematical Physics II: Fourier Analysis, Self-Adjointness* sAcademic,

New York, 1975d. 6 M. Reed and B. Simon, *Methods of Modern Mathematical Physics I: Functional Analysis* sAcademic, New York, 1972d.

