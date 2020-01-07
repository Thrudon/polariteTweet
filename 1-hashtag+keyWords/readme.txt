Suivant l'ordre chronologique:
- annotautoxml.py utilise les fichiers tweetsTest et tweetsTrain précedents pour créer dataTest.xml et dataTrain.xml, qui sont les fichiers annotés.
- create_lexique.py utilise les fichiers générés précédement pour créer un index (index_extract.txt) et l'utilise pour mettre les xml au format SVM.

Il faut ensuite entrainer le modèle SVM, sortir le modèle et l'utiliser sur les données de test:
../liblinear-2.30/train –c 4 –e 0.1 –v 5 svm_Train.svm
../liblinear-2.30/train –c 4 –e 0.1 svm_Train.svm tweets.model
../liblinear-2.30/predict svm_Test.svm tweets.model out.txt 

Ainsi on génere le fichier out.txt qui possède les polarités estimées.
Il faut cependant les mettre en forme pour évaluation.
- associate_pred.py permet de lier les ids des tweets aux résultats et sort un fichier res.txt prêt pour évaluation.
