export BERT_BASE_DIR=/mnt/raid5/data3/sywang/work/5mC_pred/BERT-Base
python3 extract_features.py \
  --input_file=/mnt/raid5/data2/sywang/5mc/feature/test_neg2.txt \
  --output_file=/mnt/raid5/data2/sywang/5mc/extra/fin_feature/test_neg2.json \
  --layers=-1 \
  --vocab_file=$BERT_BASE_DIR/vocab/vocab_3kmer.txt \
  --bert_config_file=$BERT_BASE_DIR/bert_config_3.json \
  --init_checkpoint=/mnt/raid5/data2/sywang/5mc/fine_tune/5mc-3/test/model.ckpt-89332 \
  --max_seq_length=128 \
  --batch_size=32
