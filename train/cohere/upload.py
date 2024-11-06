import constants
import cohere

co = cohere.ClientV2(constants.COHERE_AI_ACCESS_KEY)

datasets = co.datasets.list()
for _, dataset in datasets:
    print(f"dataset= {dataset[0]}")
    print(f"Dataset ID: {dataset[0].id}")
    print(f"Dataset Name: {dataset[0].name}")
    print(f"Dataset Type: {dataset[0].dataset_type}")

# Single train file upload
# print("Current Working Directory:", os.getcwd())
# chat_dataset = co.datasets.create(name="chat-training",
#                                    data=open("assets/cohere/training_combination_1.jsonl", "rb"),
#                                    type="chat-finetune-input")
# print(co.wait(chat_dataset))

# # Uploading both train and eval file
# chat_dataset_with_eval = co.datasets.create(name="chat-dataset-with-eval",
#                                            data=open("path/to/train.jsonl, "rb"),
#                                            eval_data=open("path/to/eval.jsonl, "rb"),
#                                            type="chat-finetune-input")

# print(co.wait(chat_dataset_with_eval))

