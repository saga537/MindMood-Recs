from sentence_transformers import SentenceTransformer, util

# Load model once when the script starts
model = SentenceTransformer('all-MiniLM-L6-v2')

# Predefined emotional themes (lowercased for consistency)
themes = [
    "anxiety", "depression", "heartbreak", "loss of a loved one", "grief", "loneliness", 
    "fear of failure", "lack of confidence", "career confusion", "burnout", "existential crisis", 
    "motivation", "self-worth issues", "identity crisis", "self-discovery", "decision making stress", 
    "overthinking", "fear of rejection", "feeling stuck", "uncertainty about the future", 
    "low self-esteem", "imposter syndrome", "healing from trauma", "letting go", "forgiveness", 
    "trust issues", "broken relationships", "seeking inspiration", "need for courage", 
    "creative block", "sadness", "stressed", "peaceful", "romantic", "excited", "inspired", 
    "happy", "joy", "motivated", "angry", "adventurous", "hopeful", "nostalgic", "guilty", 
    "self-criticism", "curiosity", "creative", "disappointment", "love", "dreamy", "epic",
    "suspense", "meloncholic", "energetic", "action", "romance", "comedy", "space", "science fiction",
    "adventure", "drama", "horror", "fantasy", "animation", "mystery", "thriller", 
    "biography", "history", "technology", "emptiness", "calm", "relax", "boredom", 
    "fun", "excitement", "party", "inspiration", "uplifting", "chill", "old hits"
]

def detect_theme(user_input):
    # Normalize input
    cleaned_input = user_input.strip().lower()

    # Convert user input and themes to embeddings
    user_embedding = model.encode(cleaned_input, convert_to_tensor=True)
    theme_embeddings = model.encode(themes, convert_to_tensor=True)

    # Compute cosine similarity
    scores = util.cos_sim(user_embedding, theme_embeddings)[0]
    best_match_index = scores.argmax()
    best_theme = themes[best_match_index]

    print(f"DEBUG: Input='{cleaned_input}', Matched Theme='{best_theme}'")  # Optional logging
    return best_theme
