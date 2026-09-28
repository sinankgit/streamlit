import streamlit as st

# 150 words structured into a 30-day Python dictionary
vocab_data = {
    "Day 1": {
        "Advocate": "To support publicly",
        "Ambiguous": "Open to multiple interpretations",
        "Articulate": "To express ideas clearly",
        "Assert": "To state a fact or belief confidently",
        "Candid": "Truthful and straightforward"
    },
    "Day 2": {
        "Compelling": "Evoking interest in a powerful way",
        "Consensus": "General agreement",
        "Contemplate": "To think profoundly and at length",
        "Contradict": "To assert the opposite of",
        "Convey": "To make an idea understandable"
    },
    "Day 3": {
        "Deduce": "To draw a logical conclusion",
        "Elaborate": "To develop or present in detail",
        "Scrutinize": "To examine closely and thoroughly",
        "Skeptical": "Not easily convinced; having doubts",
        "Subjective": "Based on personal feelings or opinions"
    },
    "Day 4": {
        "Eloquent": "Fluent and persuasive in speaking",
        "Emphasize": "To give special importance to",
        "Evaluate": "To assess or judge",
        "Infer": "To deduce from evidence",
        "Nuance": "A subtle difference in meaning"
    },
    "Day 5": {
        "Perceive": "To become aware of or understand",
        "Perspective": "A particular point of view",
        "Persuasive": "Good at convincing others",
        "Plausible": "Seeming reasonable or probable",
        "Profound": "Very great or intense"
    },
    "Day 6": {
        "Rationalize": "To justify an action or attitude",
        "Reiterate": "To say something again for clarity",
        "Unbiased": "Showing no prejudice; impartial",
        "Validate": "To check or prove the accuracy of",
        "Witty": "Showing quick and inventive verbal humor"
    },
    "Day 7": {
        "Acquire": "To buy or obtain",
        "Adaptable": "Able to adjust to new conditions",
        "Allocate": "To distribute resources or duties",
        "Analytical": "Relating to logical reasoning",
        "Catalyst": "A person or thing that precipitates change"
    },
    "Day 8": {
        "Collaborate": "To work jointly on an activity or project",
        "Compile": "To produce by assembling information",
        "Constraint": "A limitation or restriction",
        "Coordinate": "To bring different elements into harmony",
        "Criterion": "A principle or standard by which something is judged"
    },
    "Day 9": {
        "Delegate": "To entrust a task or responsibility to another",
        "Discrepancy": "An illogical or surprising lack of compatibility",
        "Execute": "To put a plan, order, or course of action into effect",
        "Feasible": "Possible to do easily or conveniently",
        "Implement": "To put a decision or plan into effect"
    },
    "Day 10": {
        "Innovative": "Featuring new methods or ideas",
        "Meticulous": "Showing great attention to detail",
        "Milestone": "A significant stage or event",
        "Optimize": "To make the best or most effective use of",
        "Pioneer": "To be the first to use or apply a new method"
    },
    "Day 11": {
        "Prerequisite": "A thing required as a prior condition",
        "Proficient": "Competent or skilled in doing something",
        "Requisite": "Made necessary by particular regulations",
        "Rigorous": "Extremely thorough, exhaustive, or accurate",
        "Streamline": "To make an organization or system more efficient"
    },
    "Day 12": {
        "Synthesize": "To combine a number of things into a coherent whole",
        "Versatile": "Able to adapt or be adapted to many different functions",
        "Viable": "Capable of working successfully; feasible",
        "Inherent": "Existing in something as a permanent attribute",
        "Initiative": "The power or opportunity to act or take charge"
    },
    "Day 13": {
        "Affluent": "Having a great deal of money; wealthy",
        "Amiable": "Having or displaying a friendly and pleasant manner",
        "Astute": "Having an ability to accurately assess situations",
        "Authentic": "Of undisputed origin; genuine",
        "Charismatic": "Exercising a compelling charm that inspires devotion"
    },
    "Day 14": {
        "Compassionate": "Feeling or showing sympathy and concern for others",
        "Dynamic": "Characterized by constant change, activity, or progress",
        "Empathetic": "Showing an ability to understand and share the feelings of another",
        "Exuberant": "Filled with or characterized by a lively energy and excitement",
        "Gregarious": "Fond of company; sociable"
    },
    "Day 15": {
        "Cultivate": "To try to acquire or develop (a quality, sentiment, or skill)",
        "Foster": "To encourage or promote the development of",
        "Flourish": "To grow or develop in a healthy or vigorous way",
        "Mitigate": "To make less severe, serious, or painful",
        "Navigate": "To plan and direct the route or course of action"
    },
    "Day 16": {
        "Introverted": "Tending to turn inward mentally",
        "Observant": "Quick to notice things",
        "Pragmatic": "Dealing with things sensibly and realistically",
        "Quirky": "Characterized by peculiar or unexpected traits",
        "Resilient": "Able to withstand or recover quickly from difficult conditions"
    },
    "Day 17": {
        "Stoic": "Enduring pain and hardship without showing one's feelings",
        "Tenacious": "Tending to keep a firm hold of something; clinging or adhering closely",
        "Vibrant": "Full of energy and enthusiasm",
        "Wholesome": "Conducive to or suggestive of good health and physical well-being",
        "Mutual": "Held in common by two or more parties"
    },
    "Day 18": {
        "Endure": "To suffer (something painful or difficult) patiently",
        "Resonate": "To produce or be filled with a deep, full, reverberating sound or emotion",
        "Savor": "To taste (good food or drink) and enjoy it completely",
        "Alleviate": "To make (suffering, deficiency, or a problem) less severe",
        "Paramount": "More important than anything else"
    },
    "Day 19": {
        "Abundant": "Existing or available in large quantities",
        "Aesthetics": "A set of principles concerned with the nature and appreciation of beauty",
        "Bustling": "Full of energetic and noisy activity",
        "Chaotic": "In a state of complete confusion and disorder",
        "Commute": "A regular journey of some distance to and from one's place of work"
    },
    "Day 20": {
        "Contemporary": "Living or occurring at the same time; belonging to the present",
        "Cosmopolitan": "Including or containing people from many different countries",
        "Deteriorate": "To become progressively worse",
        "Diverse": "Showing a great deal of variety",
        "Escalating": "Increasing rapidly"
    },
    "Day 21": {
        "Fluctuate": "To rise and fall irregularly in number or amount",
        "Inevitable": "Certain to happen; unavoidable",
        "Obsolete": "No longer produced or used; out of date",
        "Picturesque": "Visually attractive, especially in a quaint or pretty style",
        "Volatile": "Liable to change rapidly and unpredictably"
    },
    "Day 22": {
        "Predominant": "Present as the strongest or main element",
        "Pristine": "In its original condition; unspoiled",
        "Prominent": "Important; famous",
        "Proportionate": "Corresponding in size or amount to something else",
        "Rural": "In, relating to, or characteristic of the countryside"
    },
    "Day 23": {
        "Serene": "Calm, peaceful, and untroubled",
        "Stagnant": "Having no current or flow and often having an unpleasant smell",
        "Suburban": "Characteristic of a suburb",
        "Sustainable": "Able to be maintained at a certain rate or level",
        "Tangible": "Perceptible by touch"
    },
    "Day 24": {
        "Tedious": "Too long, slow, or dull; tiresome or monotonous",
        "Tranquil": "Free from disturbance; calm",
        "Ubiquitous": "Present, appearing, or found everywhere",
        "Unprecedented": "Never done or known before",
        "Urban": "In, relating to, or characteristic of a city or town"
    },
    "Day 25": {
        "Accordingly": "In a way that is appropriate to the particular circumstances",
        "Admittedly": "Used to introduce a concession or recognition that something is true",
        "Albeit": "Although",
        "Consequently": "As a result",
        "Conversely": "Introducing a statement or idea which reverses one that has just been made"
    },
    "Day 26": {
        "Crucially": "With decisive or vital importance",
        "Furthermore": "In addition; besides",
        "Hence": "As a consequence; for this reason",
        "Initially": "At first",
        "Invariably": "In every case or on every occasion; always"
    },
    "Day 27": {
        "Likewise": "In the same way; also",
        "Marginal": "Minor and not important; not central",
        "Moreover": "As a further matter; besides",
        "Widespread": "Found or distributed over a large area or number of people",
        "Whereas": "In contrast or comparison with the fact that"
    },
    "Day 28": {
        "Namely": "That is to say; to be specific",
        "Nevertheless": "In spite of that; notwithstanding",
        "Nominal": "Existing in name only; very small",
        "Nonetheless": "In spite of that; nevertheless",
        "Notably": "Especially; in particular"
    },
    "Day 29": {
        "Pivotal": "Of crucial importance in relation to the development or success of something else",
        "Predominantly": "Mainly; for the most part",
        "Presumably": "Used to convey that what is asserted is very likely though not known for certain",
        "Subsequent": "Coming after something in time; following",
        "Substantial": "Of considerable importance, size, or worth"
    },
    "Day 30": {
        "Ultimately": "Finally; in the end",
        "Undoubtedly": "Without doubt; certainly",
        "Via": "Traveling through (a place) en route to a destination",
        "Synthesize": "To combine a number of things into a coherent whole",
        "Elaborate": "To develop or present in detail"
    }
}

# --- Streamlit App UI ---
st.set_page_config(page_title="30-Day Vocab Builder", page_icon="📚")

st.title("📚 30-Day Vocabulary Builder")
st.write("Learn 5 words a day. Check the box once you successfully use the word in a conversation or speech!")

# Sidebar for navigation
st.sidebar.header("Navigation")
day_list = list(vocab_data.keys())
selected_day = st.sidebar.selectbox("Select your day:", day_list)

# Main content area
st.header(selected_day)
st.divider()

words_for_day = vocab_data[selected_day]

# Display the 5 words with an interactive checkbox
for word, meaning in words_for_day.items():
    col1, col2 = st.columns([3, 1])
    
    with col1:
        st.subheader(word)
        st.write(f"*{meaning}*")
        
        # Generates a dynamic URL to Vocabulary.com
        dict_url = f"https://www.vocabulary.com/dictionary/{word.lower()}"
        st.markdown(f"[📖 See examples & explanation]({dict_url})")
        
    with col2:
        # Initialize session state for the checkbox if it doesn't exist
        if word not in st.session_state:
            st.session_state[word] = False
            
        # Checkbox updates session state automatically
        st.checkbox("Used today!", key=word)
        
    st.divider()

# Progress tracker in the sidebar
st.sidebar.divider()
st.sidebar.subheader("Overall Progress")
total_words = 150
words_used = sum(1 for key, value in st.session_state.items() if value is True)
progress = words_used / total_words

st.sidebar.progress(progress)
st.sidebar.write(f"**{words_used} / {total_words}** words practiced in real life.")
