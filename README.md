Welcome to this repository! Here you will find two sub-repositories, old_daic_woz and avec. Each is a NLP / linguistic approach to modelling a version of the [DAIC-WOZ](http://dcapswoz.ict.usc.edu/) dataset with PHQ8 scores (now replaced by [PHQ-9](https://en.wikipedia.org/wiki/PHQ-9) scores). The two repositories clean, process, explore, and use models in scikit-learn to try and predict PHQ-8 scores from the transcripts of participants. However, the old_daic_woz repository does so on older DAIC-WOZ data (a previous release), while the avec repository analyzes data released in 2019.

The processing steps for the newly-released DAIC-WOZ data set for the [2019 AVEC challenge](https://sites.google.com/view/avec2019/home?authuser=0) follow most of the same processing steps as those shown in the old_daic_woz sub-repository. However, for the old dataset I used a lot of Jupyter Notebooks to show how processing steps were carried out, as well as output from most of those steps. For the challenge's new dataset, I have included the processing steps that don't have graphical output as Python files so that they can be run from the command line.

This repository relies heavily on the most up-to-date versions of the following packages:
- Python 3.6.8
- NumPy 1.15.4
- pandas 0.24.2
- Matplotlib 3.0.3
- seaborn 0.9.0
- scikit-learn 0.20.1
- NLTK 3.4.1 
- gensim 3.4.0
- spaCy 2.0.16 (you will need it to run one of the processing methods in `clean_text.py`)


None of the data used for these two analyses was included. If you are interested in getting the data for yourself and work in academia or for other non-profits, please visit the link above for the database and review the end user license agreement.
