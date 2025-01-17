from utils import create_input_files

if __name__ == '__main__':
    # Create input files (along with word map)
    create_input_files(dataset='aicc',
                       karpathy_json_path='/workspace/data/aicc_caption/dataset_aicc.json',
                       image_folder='/workspace/data/aicc_caption/images',
                       captions_per_image=5,
                       min_word_freq=5,
                       output_folder='/workspace/data/aicc_caption/',
                       max_len=50)
