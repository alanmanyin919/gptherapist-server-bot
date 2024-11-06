import constants
import cohere
from cohere.finetuning import Hyperparameters, Settings, FinetunedModel, BaseModel, WandbConfig

co = cohere.ClientV2(constants.COHERE_AI_ACCESS_KEY)

hp = Hyperparameters(
  early_stopping_patience=10,
  early_stopping_threshold=0.001,
  train_batch_size=16,
  train_epochs=1,
  learning_rate=0.01,
)

# optional (define wandb configuration)
# wnb_config = WandbConfig(
#     project="test-project",
#     api_key="<<wandbApiKey>>",
#     entity="test-entity",
# )


create_response = co.finetuning.create_finetuned_model(
  request=FinetunedModel(
    name="customer-service-chat-model",
    settings=Settings(
      base_model=BaseModel(
        base_type="BASE_TYPE_CHAT",
      ),
      dataset_id="chat-training-3fdvvw",
      hyperparameters=hp,
    #   wandb=wnb_config,
    ),
  ),
)

