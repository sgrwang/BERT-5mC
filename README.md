1. Pretraining Promoter-BERT model 
python3 generated_ngram_supervised.py in_file out_file 3 #Processing data
python3 make-pre-train-model.py #Pretraining

2. Fine tuning 
python3 generated_ngram_supervised2.py in_file out_file 3 #Processing data
chmod +x ./run_fine_tune.sh
./run_fine_tune.sh #Fine tuning
