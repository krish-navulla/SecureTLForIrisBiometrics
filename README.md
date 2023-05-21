# SecureTLForIrisBiometrics Project Repository

**Implementing The Secure Triplet Loss For Template Cancelebility In Iris Biometrics**    
Vamshi Krishna Navulla    
*Department of Computer Science and Engineering University at Buffalo*   
vnavulla@buffalo.edu

## Summary
(1) **Data Preprocessing**  
The data pre-processsing is done in the aux_functions.py, when called from the iris_prepare_AMF_inception.py. Also, the images are transformed in the dataset.py when called from the trainer scripts.  
(2)**Fine Tuning**  
Fine Tuning The models are loaded in the models.py in their respective init functions. The freeze member functions are responsible for freezing the layers.  
(3) **Training**  
Training The traning is done in respective scripts, iris_secure_Inception/iris_secure_attention for inception resnet and Vit models respectively.  
(3) **Results**  
Results The results are shown with the help of result_analysis.py, where it calls the required plotting functions from the aux_functions.py script.  

## Acknowledgements
This repository is forked from the parent repository, from where the majority of the code was referenced from [[link]](https://github.com/jtrpinto/SecureTL),  which was published as part of their paper referenced below [[pdf]](https://jtrpinto.github.io/files/pdf/jpinto2021tbiom.pdf)

**J. R. Pinto, M. V. Correia, and J. S. Cardoso, "Secure Triplet Loss: Achieving Cancelability and Non-Linkability in End-to-End Deep Biometrics", in *IEEE Transactions on Biometrics, Behavior, and Identity Science,* 3(2): pp. 180-189, 2021.**    
[[link]](https://ieeexplore.ieee.org/document/9302588) [[pdf]](https://jtrpinto.github.io/files/pdf/jpinto2021tbiom.pdf) [[bib]](https://jtrpinto.github.io/files/bibtex/jpinto2021tbiom.bib)    

**J. R. Pinto, J. S. Cardoso, and M. V. Correia, "Secure Triplet Loss for End-to-End Deep Biometrics", in *8th International Workshop on Biometrics and Forensics (IWBF 2020),* 2020.**    
[[link]](https://ieeexplore.ieee.org/document/9107958) [[pdf]](https://jtrpinto.github.io/files/pdf/jpinto2020iwbf.pdf) [[bib]](https://jtrpinto.github.io/files/bibtex/jpinto2020iwbf1.bib)

## References
(1) Pinto, J.R.; Cardoso, J.S.; Correia, M.V.: Secure Triplet Loss for End-to-End Deep Biometrics. 8th International Workshop on Biometrics and Forensics (IWBF 2020), 2020.    
(2) Chechik, G.; Sharma, V.; Shalit, U.; Bengio, S.: Large scale onlinelearning of image similarity through ranking. Journal of Machine Learning Research, 11:1109-1135, 2010.    
(3) Pinto, J.R.; Correia, M.V.; Cardoso, J.S.: J. R. Pinto, M. V. Correia, and J. S. Cardoso, "Secure Triplet Loss: Achieving Cancelability and Non-Linkability in End-to-End Deep Biometrics". IEEE Transactions on Biometrics, Behavior, and Identity Science, 3(2):180-189, 2021.    
(4) Wolf, L.; Hassner, T.; Maoz, I.: Face Recognition in Unconstrained Videos with Matched Background Similarity. IEEE Conference on Computer Vision and Pattern Recognition (CVPR), 2011.    
(5) Wahabi, S.; Pouryayevali, S.; Hari, S.; Hatzinakos, D.: On Evaluating ECG Biometric Systems: Session-Dependence and Body Posture. IEEE Transactions on Information Forensics and Security, 9(11):2002–2013, Nov 2014. 






