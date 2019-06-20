Welcome to this repository! Here you will find two sub-repositories, old_daic_woz and avec. Each is a NLP/linguistic approach to modelling a version of the [DAIC-WOZ](http://dcapswoz.ict.usc.edu/) dataset with PHQ8 scores (now replaced by [PHQ-9](https://en.wikipedia.org/wiki/PHQ-9) scores). The two repositories clean, process, explore, and use models in scikit-learn to try and predict PHQ-8 scores from the transcripts of participants. However, the old_daic_woz repository does so on older DAIC-WOZ data (a previous release), while the avec repository analyzes data released in 2019.

The processing steps for the newly-released DAIC-WOZ data set for the [2019 AVEC challenge](https://sites.google.com/view/avec2019/home?authuser=0) follow most of the same processing steps as those shown in the old_daic_woz sub-repository. However, for the old dataset I used a lot of Jupyter Notebooks to show how processing steps were carried out, as well as output from most of those steps. For the challenge's new dataset, I have included the processing steps that don't have graphical output as Python files so that they can be run from the command line.

This repository relies heavily on the most up-to-date versions of the following packages (as of 07.01.2019):
- Python
- NumPy
- pandas
- Matplotlib
- seaborn
- scikit-learn
- NLTK
- gensim
- spaCy (only used sparingly, but you will need it to run one of the processing methods in `clean_text.py`


None of the data used for these two analyses was included. If you are interested in getting the data for yourself and work in academia or for other non-profits, please visit the link above for the database and review the end user license agreement.
