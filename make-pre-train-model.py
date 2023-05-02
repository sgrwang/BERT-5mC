import os
import sys
sys.path.append('/mnt/raid5/data3/sywang/work/5mC_pred/BERT-Base/')

os.environ['CUDA_VISIBLE_DEVICES']='3'

#os.system('nohup python2 /mnt/raid5/data3/sywang/work/5mC_pred/BERT-Base/create_pretraining_data.py --input_file=/mnt/raid5/data3/sywang/work/5mC_pred/BERT-Base/dataset/pre-train/5mc-1/hg3_data.txt --output_file=/mnt/raid5/data2/sywang/5mc/dataset/5mc-1/pre_train/hg3_data.tfrecord --vocab_file=/mnt/raid5/data3/sywang/work/5mC_pred/BERT-Base/vocab/vocab_1kmer.txt --do_lower_case=True --max_seq_length=256 --max_predictions_per_seq=20 --masked_lm_prob=0.15 --random_seed=12345 --dupe_factor=5 > ./create_pretraining_data_1.log 2>&1 &')


os.system('nohup python2 /mnt/raid5/data3/sywang/work/5mC_pred/BERT-Base/run_pretraining.py --input_file=/mnt/raid5/data2/sywang/5mc/dataset/5mc-1/pre_train/hg3_data.tfrecord --output_dir=/mnt/raid5/data2/sywang/5mc/pre/5mc-1 --do_train=True --do_eval=True --bert_config_file=/mnt/raid5/data3/sywang/work/5mC_pred/BERT-Base/bert_config_1.json --train_batch_size=32 --max_seq_length=256 --max_predictions_per_seq=20 --num_train_steps=200000 --num_warmup_steps=10000 --learning_rate=5e-5 > ./run_pretraining_1k.log 2>&1 &')
