from app.utils.pinecone_utils import query_similar, client
from app.utils.shared_state import all_info

def chat_with_memory(query: str):
    # Retrieve similar docs
    results = query_similar(query)
    
    context = all_info

    # Combine context + user query
    prompt = f"""
You are a friendly, evidence-aware wellness coach. You will be given:
1) CONTEXT: short anonymized data snippets about the user (sleep, vitals, nutrition, labs, previous important info), if available.
2) query: the user's query.

Your task:
- Use the context to provide practical and concise (3-6 points) recommendations if user want.
- No need to make any recommendations until user ask for it.
- If the context contains relevant personal info, prioritize it in your advice.
- If context does not cover the topic, provide safe, general, evidence-based guidance on health, wellness, nutrition, exercise, sleep, mental health, or lifestyle.
- Always keep your advice friendly, concise, and actionable.
- Highlight which data points from context you used (by timestamp and source), if any.
- If there is potential clinical risk (e.g., dangerously abnormal labs, chest pain), instruct the user to seek medical attention.

CONTEXT:
{context}

query:
{query}

RESPONSE:
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful wellness assistant."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content
