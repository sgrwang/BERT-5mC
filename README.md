1. Pretraining Promoter-BERT model
#Processing data
python3 generated_ngram_supervised.py in_file out_file 3
#Pretraining
python3 make-pre-train-model.py

2. Fine tuning
#Processing data
python3 generated_ngram_supervised2.py in_file out_file 3
#Fine tuning
chmod +x ./run_fine_tune.sh
./run_fine_tune.sh

