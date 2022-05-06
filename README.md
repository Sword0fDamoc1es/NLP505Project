# BU-CS505-2022-Spring-Final-Project

## multilingual arabizi sentiment.

## File Structure

```
./code
    - arabic_bert.ipynb  # code for our ablation studies, that is comparing a range of models
    - arabizi2arabic.py  # code for transliterating Arabizi to Arabic, by using Yamli API
    - data_preprocessing.ipynb  # code for transforming raw datasets into the standard form for our project
    - train_xml_roberta.ipynb  # code for reproducing our primary results
    
./datasets
    - arabic-english-6k/
    - arabizi-english-60k/
    - semeval2017-arabic/
    - semeval2017-english/
```

## Training XML RoBERTa

**Step 1:** Upload train_xml_roberta.ipynb from ./code to Google Colab and open it.
**Step 2:** Upload all the contents from ./datasets/arabizi-english-60k, to the current directory of your Colab environment
**Step 3:** Execute the notebook from the first line.
