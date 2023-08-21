# BERT-5mC: an interpretable model for predicting 5-methylcytosine sites of DNA based on BERT
**Authors**: Shuyu Wang, Yinbo Liu, Yufeng Liu, Yong Zhang, and Xiaolei Zhu
Code of our paper: [BERT-5mC: an interpretable model for predicting 5-methylcytosine sites of DNA based on BERT].


# Table of Contents
- **[Reproduce Results](#reproduce-results )**<br>
    - **[Pre-training](#pre-training)**<br>
    - **[Fine-tuning](#fine-tuning)**<br>
    - **[Extract embedding ](#extract-embedding)**<br>
- **[Example Usage](#example-usage)**<br>
    - **[Environment Setup](#environment-setup)**<br>
    - **[Data Preparation](#data preparation)**<br>
    - **[Start predicting ](#start-predicting)**<br>
- **[Getting Help](#getting-help)**<br>

# Reproduce Results

## Pre-training

Layout environment variables.

```sh
$ python version: 2.7
$ pip3 install -r requirements.txt
```

Before pre-training, we preprocess the collected human promoter sequence samples using word segmentation methods to ensure that the sequence data can be successfully input into the BERT model for training.

```sh
$ python generated_ngram_supervised.py in_file out_file ngrm
```

Start pre-training

```sh
$ chmod +x ./create_pretraining_data.sh
$ ./create_pretraining_data.sh
$ chmod +x ./pre_training.sh
$ ./pre_training.sh
```
After pre-trained, we obtained a new pre training model that focuses on the DNA promoter sequence region, called the Promoter_ BERT. Based on Promoter_ BERT, we attempted two strategic methods to predict the 5mC site on the human promoter sequence.

## Fine-tuning

Based on Promoter-BERT，We use the  5mC training dataset to fine-tuning the BERT model, and use the fine-tuned model to predict the independent test set. Environment Setup:

```sh
$ python version: 3.6
$ pip3 install -r requirements2.txt
```

Similarly, preprocess the DNA sequence sample data and label each sample data (if the DNA sequence sample contains a 5mC site, the label is 1, otherwise it is 0)

```sh
$ python generated_ngram_supervised2.py in_file out_file ngrm
```

Start fine-tuning

```sh
$ chmod +x ./run_fine_tune.sh
$ ./run_fine_tune.sh
```
Save the prediction results in this file: test_results.tsv

## Extract embedding 

Extract BERT embeddings as features and combine them with machine learning algorithms or deep learning algorithms to train the model. 

Preprocessing sample data:

```sh
$ python generated_ngram_supervised2.py in_file out_file ngrm
```

Extracting the embedding of “CLS” token.

```sh
$ chmod +x ./extract_features.sh
$ ./extract_features.sh 
$ python extra_fea.py
```

Or,  extract average embedding for all words of a DNA sequence.

```sh
$ chmod +x ./extract_features.sh
$ ./extract_features.sh 
$ python3 extra_avg_fea.py
```

We extracted BERT embeddings from both the Promoter BERT model and the fine-tuned model for experiments. In addition, we also calculated the nucleotide nature and frequency (NPF)  features. 


# Example Usage

Example: How to use the model BERT-5mC to predict whether a 41bp DNA sequence contains a 5mC site.

## Environment Setup

BERT-5mC requires [Python version 3.6 or higher].

```sh
$ python version: 3.6
$ pip3 install -r requirements2.txt
```

## Data Preparation

```sh
$ python generated_ngram_supervised.py  example.fasta test.tsv 3
```

## Start predicting 

BERT-5mC achieves prediction of 5mC sites by fine-tuning the Promoter-BERT model.

```sh
$ chmod +x ./predict.sh
$ ./predict.sh
```
Save the prediction results in this file: test_results.tsv


# Getting help
We appreciate your feedback and questions! Thank you!
