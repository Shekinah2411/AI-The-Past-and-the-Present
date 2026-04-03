import torch
from transformers import AutoModelForCausalLM, AutoTokenizer


MODEL_NAME = "Qwen/Qwen2.5-1.5B-Instruct"
SYSTEM_PROMPT = (
    "You are a helpful instruction-following assistant in a chatbot comparison lab. "
    "Respond conversationally to the user's message, keep answers concise, and avoid "
    "roleplay formatting like 'User:' or 'Assistant:'."
)

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, local_files_only=True)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME, local_files_only=True)
model.eval()

conversation_history = [
    {"role": "system", "content": SYSTEM_PROMPT},
]


def get_llm_response(user_input: str) -> str:
    conversation_history.append({"role": "user", "content": user_input})

    prompt_text = tokenizer.apply_chat_template(
        conversation_history,
        tokenize=False,
        add_generation_prompt=True,
    )
    model_inputs = tokenizer(prompt_text, return_tensors="pt")

    with torch.no_grad():
        generated_ids = model.generate(
            model_inputs["input_ids"],
            attention_mask=model_inputs["attention_mask"],
            max_new_tokens=120,
            do_sample=True,
            temperature=0.7,
            top_p=0.9,
            pad_token_id=tokenizer.eos_token_id,
        )

    prompt_length = model_inputs["input_ids"].shape[-1]
    new_tokens = generated_ids[0][prompt_length:]
    assistant_text = tokenizer.decode(new_tokens, skip_special_tokens=True).strip()
    conversation_history.append({"role": "assistant", "content": assistant_text})
    return assistant_text


def reset_llm_conversation() -> None:
    conversation_history.clear()
    conversation_history.append({"role": "system", "content": SYSTEM_PROMPT})


if __name__ == "__main__":
    print("Modern AI Chatbot")
    print("Type 'quit' to stop.\n")

    while True:
        user = input("You: ").strip()

        if user.lower() == "quit":
            print("Bot: Goodbye!")
            break

        print("Bot:", get_llm_response(user))
