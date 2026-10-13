"""
Question bank - DSC401-6 Artificial Intelligence, Units I & II.
All questions are kept basic and in simple language. Levels (Easy / Medium / Hard)
only change how much thinking is needed, not how advanced the topic is.
"""

AR_OPTIONS = [
    "Both A and R are true, and R explains A",
    "Both A and R are true, but R does NOT explain A",
    "A is true, R is false",
    "A is false, R is true",
]
TF_OPTIONS = ["True", "False"]

QUESTIONS = []


def add(qtype, topic, level, q, answer, exp, hint, options=None, pairs=None,
        accept=None, real=False, search=False):
    QUESTIONS.append(dict(type=qtype, topic=topic, level=level, q=q, answer=answer,
                          exp=exp, hint=hint, options=options, pairs=pairs,
                          accept=accept, real=real, search=search))


# ============================ FOUNDATIONS & APPLICATIONS ============================
add("MCQ", "Foundations & Applications", "Easy",
    "What is Artificial Intelligence (AI)?",
    "Making machines act intelligently like humans",
    "AI is about making machines think, learn, and make decisions like humans.",
    "Think: machine + human-like intelligence.",
    options=["Making machines act intelligently like humans", "Making computers faster",
             "Storing lots of data", "Building bigger screens"])

add("MCQ", "Foundations & Applications", "Easy",
    "Which of these is an example of AI?",
    "Voice assistant like Siri or Alexa",
    "Voice assistants understand speech and reply, so they use AI.",
    "Which one understands what you say?",
    options=["Voice assistant like Siri or Alexa", "A normal calculator", "A table fan", "A paper notebook"])

add("Scenario", "Foundations & Applications", "Medium",
    "Netflix suggests movies based on what you watched before. Which AI application is this?",
    "Recommendation system",
    "A recommendation system learns your taste from past data and suggests similar items.",
    "It recommends things for you.",
    options=["Recommendation system", "Self-driving car", "Chess player", "Robot arm"],
    real=True)

add("Scenario", "Foundations & Applications", "Hard",
    "A hospital app looks at an X-ray image and tells whether there is a disease. Which AI field is used mainly?",
    "Computer vision",
    "Understanding images is called computer vision.",
    "The input is a picture.",
    options=["Computer vision", "Speech recognition", "Game playing", "Text translation"],
    real=True)

# ============================ TURING TEST ============================
add("MCQ", "Turing Test", "Easy",
    "Who proposed the Turing Test?",
    "Alan Turing",
    "Alan Turing proposed the test in 1950 to check whether a machine can think.",
    "The name is in the question.",
    options=["Alan Turing", "John McCarthy", "Newton", "Charles Babbage"])

add("MCQ", "Turing Test", "Easy",
    "In the Turing Test, a machine passes when...",
    "A human cannot tell if it is a machine or a person",
    "If the judge cannot find out who is the machine, the machine passes.",
    "It is about fooling the judge.",
    options=["A human cannot tell if it is a machine or a person", "It plays chess well",
             "It is very fast", "It has a lot of memory"])

add("True/False", "Turing Test", "Medium",
    "The basic Turing Test is done through text conversation (typing).",
    "True",
    "The judge chats with a human and a machine through text, so voice and body are not needed.",
    "Think of a chat window.",
    options=TF_OPTIONS)

add("Scenario", "Turing Test", "Hard",
    "You chat with a customer-care chatbot and cannot tell if it is a person or a bot. Which test is this similar to?",
    "Turing Test",
    "Not being able to tell machine from human is exactly what the Turing Test checks.",
    "Same idea as 'can the machine fool you?'",
    options=["Turing Test", "Hill climbing", "Goal test", "BFS test"],
    real=True)

# ============================ RATIONAL AGENTS ============================
add("MCQ", "Rational Agents", "Easy",
    "A rational agent is an agent that...",
    "Does the right thing to get the best result",
    "A rational agent picks the action that is expected to give the best performance.",
    "Rational = does the best possible thing.",
    options=["Does the right thing to get the best result", "Acts randomly", "Never makes any mistake ever",
             "Only follows orders"])

add("True/False", "Rational Agents", "Medium",
    "A rational agent must know the future and never make a mistake.",
    "False",
    "Rational does not mean all-knowing. It means choosing the best action using what the agent knows.",
    "Can anyone know the future?",
    options=TF_OPTIONS)

add("Assertion-Reason", "Rational Agents", "Hard",
    "Assertion (A): A rational agent can still fail sometimes.\n\n"
    "Reason (R): Rationality means best expected result, not a guaranteed result.",
    AR_OPTIONS[0],
    "The agent chooses the best action with its knowledge, but luck or missing information can still cause failure.",
    "Expected result is not the same as actual result.",
    options=AR_OPTIONS)

# ============================ INTELLIGENT AGENTS ============================
add("MCQ", "Intelligent Agents", "Easy",
    "An agent perceives the environment through ______ and acts through ______.",
    "Sensors, actuators",
    "Sensors take input (camera, mic). Actuators perform actions (wheels, arms).",
    "Eyes and hands of a robot.",
    options=["Sensors, actuators", "Actuators, sensors", "Memory, disk", "Keyboard, mouse only"])

add("Fill in the Blanks", "Intelligent Agents", "Easy",
    "The things an agent uses to see or sense the world (like camera, microphone) are called ________.",
    "sensors",
    "Sensors collect information from the environment.",
    "Starts with 's'.",
    accept=["sensors", "sensor"])

add("Match the Following", "Intelligent Agents", "Medium",
    "Match the agent type with its meaning.",
    "See pairs",
    "Simple reflex reacts to now; model-based remembers; goal-based plans for a goal; utility-based picks the best.",
    "Think: react, remember, plan, choose best.",
    pairs=[("Simple reflex agent", "Reacts to what it sees right now"),
           ("Model-based agent", "Remembers things about the world"),
           ("Goal-based agent", "Plans actions to reach a goal"),
           ("Utility-based agent", "Chooses the action that gives the most happiness")])

add("Fill in the Blanks", "Intelligent Agents", "Hard",
    "The full form of PEAS is Performance measure, Environment, Actuators and ________.",
    "Sensors",
    "PEAS describes any agent task: Performance, Environment, Actuators, Sensors.",
    "It is the 'S' in PEAS.",
    accept=["sensors", "sensor"])

# ============================ AGENTS & ENVIRONMENTS ============================
add("Scenario", "Agents & Environments", "Easy",
    "A room thermostat turns the heater ON when it is cold and OFF when it is warm. What type of agent is it?",
    "Simple reflex agent",
    "It just reacts to the current temperature with a rule, with no memory or planning.",
    "It follows simple IF-THEN rules.",
    options=["Simple reflex agent", "Goal-based agent", "Utility-based agent", "Learning agent"],
    real=True)

add("Scenario", "Agents & Environments", "Medium",
    "A robot vacuum remembers which rooms it has already cleaned. What type of agent is it?",
    "Model-based agent",
    "It keeps a memory (model) of the house, so it is a model-based agent.",
    "It remembers something about the world.",
    options=["Simple reflex agent", "Model-based agent", "Table agent", "Human agent"],
    real=True)

add("Scenario", "Agents & Environments", "Hard",
    "A GPS app picks the route which is best by comparing time, distance and toll cost. What type of agent is it?",
    "Utility-based agent",
    "It compares many factors and chooses the best option, which is what a utility-based agent does.",
    "It chooses the BEST among many choices.",
    options=["Simple reflex agent", "Model-based agent", "Goal-based agent", "Utility-based agent"],
    real=True)

add("Scenario", "Agents & Environments", "Medium",
    "In a self-driving car, which of these is a sensor?",
    "Camera",
    "A camera sees the road, so it is a sensor. Steering and brakes are actuators.",
    "Which one only collects information?",
    options=["Camera", "Steering wheel", "Brake", "Horn"],
    real=True)

# ============================ GOOD BEHAVIOUR ============================
add("MCQ", "Good Behaviour", "Easy",
    "How do we measure whether an agent is doing well?",
    "Performance measure",
    "A performance measure tells how successful the agent's behaviour is.",
    "Think of marks in an exam.",
    options=["Performance measure", "Screen size", "Colour of the agent", "Price of the agent"])

add("True/False", "Good Behaviour", "Medium",
    "The performance measure should check the result we want in the environment (like a clean floor), not how busy the agent looks.",
    "True",
    "If we reward activity instead of results, the agent can cheat the system.",
    "Reward the result, not the effort.",
    options=TF_OPTIONS)

add("Scenario", "Good Behaviour", "Hard",
    "A cleaning robot gets a point for every dirt it picks up. It starts spilling dirt just to pick it up again. What is a better reward?",
    "A point for every time step the floor is clean",
    "Rewarding a clean floor makes the robot keep the floor clean instead of making new dirt.",
    "Reward the final result you want.",
    options=["A point for every time step the floor is clean", "A point for every dirt picked",
             "A point for every metre moved", "A point for every minute it runs"],
    real=True)

# ============================ NATURE OF ENVIRONMENTS ============================
add("MCQ", "Nature of Environments", "Easy",
    "If the agent can see the complete state of the environment, the environment is called...",
    "Fully observable",
    "Fully observable means the sensors give complete information. Chess is an example.",
    "Nothing is hidden.",
    options=["Fully observable", "Partially observable", "Dynamic", "Stochastic"])

add("MCQ", "Nature of Environments", "Easy",
    "Which of these is a fully observable environment?",
    "Chess",
    "In chess the whole board is visible. In poker, the other player's cards are hidden.",
    "Think of a game where nothing is hidden.",
    options=["Chess", "Poker", "Self-driving on a road", "Playing hide and seek"])

add("Match the Following", "Nature of Environments", "Medium",
    "Match the environment type with its meaning.",
    "See pairs",
    "These are the basic properties used to describe a task environment.",
    "Read each meaning carefully.",
    pairs=[("Deterministic", "Next state is fully decided by the action - no randomness"),
           ("Stochastic", "There is some randomness or uncertainty"),
           ("Static", "Environment does not change while the agent thinks"),
           ("Dynamic", "Environment can change while the agent thinks")])

add("Scenario", "Nature of Environments", "Hard",
    "A self-driving car is on a busy road. Which statement is correct?",
    "It is partially observable and dynamic",
    "The car cannot see everything and traffic keeps changing, so the environment is partially observable and dynamic.",
    "Can the car see behind every vehicle? Does traffic stand still?",
    options=["It is partially observable and dynamic", "It is fully observable and static",
             "It is fully observable and deterministic", "It is static and episodic"],
    real=True)

# ============================ PROBLEMS & PROBLEM SPACES ============================
add("MCQ", "Problems & Problem Spaces", "Easy",
    "Which of these is NOT part of a well-defined problem?",
    "Colour of the computer",
    "A problem needs an initial state, actions, a goal test and a path cost.",
    "Which one has nothing to do with solving the problem?",
    options=["Initial state", "Goal test", "Path cost", "Colour of the computer"])

add("Fill in the Blanks", "Problems & Problem Spaces", "Medium",
    "The state from where the search starts is called the ________ state.",
    "initial",
    "The search begins at the initial state and tries to reach the goal state.",
    "The opposite of 'goal'.",
    accept=["initial", "start", "initial state"])

add("MCQ", "Problems & Problem Spaces", "Hard",
    "The goal test is used to...",
    "Check if the current state is the goal",
    "After each step the search uses the goal test to decide whether to stop.",
    "It tells the search when to stop.",
    options=["Check if the current state is the goal", "Count the number of actions",
             "Calculate the path cost", "Find the first state"])

# ============================ STATE SPACE SEARCH ============================
add("MCQ", "State Space Search", "Easy",
    "What is a state space?",
    "The set of all possible states of a problem",
    "A state space contains all situations (states) the problem can be in, plus the moves between them.",
    "Space = collection of everything possible.",
    options=["The set of all possible states of a problem", "A room for computers",
             "The memory of a computer", "A type of graph paper"])

add("Problem Solving", "State Space Search", "Medium",
    "Water jug: a 4 L jug and a 3 L jug, both empty. You fill the 3 L jug and pour it into the 4 L jug. How much water is in the 4 L jug now?",
    "3 L",
    "The 3 L of water moves fully into the 4 L jug because it has enough space.",
    "Everything from the small jug fits.",
    options=["3 L", "4 L", "1 L", "0 L"],
    search=True)

add("Problem Solving", "State Space Search", "Hard",
    "Water jug (4 L and 3 L): you now have 3 L in the 4 L jug. Fill the 3 L jug and pour into the 4 L jug until it is full. How much water is left in the 3 L jug?",
    "2 L",
    "The 4 L jug needs only 1 more litre, so 3 - 1 = 2 L stays in the 3 L jug.",
    "How much space is left in the 4 L jug?",
    options=["2 L", "1 L", "3 L", "0 L"],
    search=True)

add("Scenario", "State Space Search", "Medium",
    "In Google Maps, finding a route between two cities is a search problem. What is a 'state' here?",
    "A place (location) on the map",
    "Each location is a state, moving along a road is an action, and distance or time is the cost.",
    "Where are you right now?",
    options=["A place (location) on the map", "The phone battery", "The colour of the road", "The app's name"],
    real=True)

# ============================ PRODUCTION SYSTEMS ============================
add("MCQ", "Production Systems", "Easy",
    "A production rule is written in the form...",
    "IF condition THEN action",
    "Production rules say: if this condition is true, then do this action.",
    "It is like an if-else statement.",
    options=["IF condition THEN action", "FOR loop", "WHILE true", "PRINT output"])

add("MCQ", "Production Systems", "Medium",
    "The three parts of a production system are:",
    "Global database, production rules, control strategy",
    "The database stores the current state, rules change it, and the control strategy decides which rule to use.",
    "Data + rules + a way to choose rules.",
    options=["Global database, production rules, control strategy", "Input, output, memory",
             "Sensors, actuators, environment", "Start, goal, path"])

add("MCQ", "Production Systems", "Hard",
    "If many rules can be applied at the same time, who decides which rule to use?",
    "Control strategy",
    "The control strategy chooses one rule from the applicable rules.",
    "It controls the order of rules.",
    options=["Control strategy", "Global database", "Goal state", "Sensors"])

# ============================ PROBLEM CHARACTERISTICS ============================
add("MCQ", "Problem Characteristics", "Easy",
    "In the 8-puzzle, if you make a wrong move you can move the tile back. Such a problem is called...",
    "Recoverable",
    "Moves that can be undone make the problem recoverable.",
    "Can you undo the move?",
    options=["Recoverable", "Irrecoverable", "Ignorable", "Impossible"])

add("MCQ", "Problem Characteristics", "Medium",
    "In chess, once you make a move it cannot be taken back. Such a problem is called...",
    "Irrecoverable",
    "Moves that cannot be undone make the problem irrecoverable.",
    "The opposite of recoverable.",
    options=["Irrecoverable", "Recoverable", "Ignorable", "Decomposable"])

add("True/False", "Problem Characteristics", "Hard",
    "In the Travelling Salesman Problem we need the SHORTEST route, so it is a 'best-path' problem.",
    "True",
    "Any route is not enough; we must find the best (shortest) one.",
    "Is any route okay, or must it be the shortest?",
    options=TF_OPTIONS)

# ============================ ISSUES IN SEARCH PROGRAM DESIGN ============================
add("MCQ", "Issues in Search Program Design", "Easy",
    "Searching from the start state towards the goal is called...",
    "Forward search",
    "Forward search starts at the initial state. Backward search starts at the goal.",
    "Start to goal.",
    options=["Forward search", "Backward search", "Random search", "Circular search"])

add("Fill in the Blanks", "Issues in Search Program Design", "Medium",
    "Searching from the goal back to the start is called ________ search.",
    "backward",
    "In backward search we begin at the goal and work towards the start state.",
    "Opposite of forward.",
    accept=["backward", "backward search"])

add("MCQ", "Issues in Search Program Design", "Hard",
    "Why do we remember the states we have already visited?",
    "To avoid visiting the same state again and again",
    "Without a visited list, the search may go in loops and waste time.",
    "Think about going round in circles.",
    options=["To avoid visiting the same state again and again", "To make the search slower",
             "To change the goal", "To print the output"])

# ============================ BFS ============================
add("MCQ", "Breadth-First Search", "Easy",
    "BFS uses which data structure?",
    "Queue",
    "BFS visits nodes in first-in-first-out order, so it uses a queue.",
    "First come, first served.",
    options=["Queue", "Stack", "Array only", "Tree only"])

add("True/False", "Breadth-First Search", "Medium",
    "BFS explores the nodes level by level.",
    "True",
    "BFS visits all nodes at one depth before going to the next depth.",
    "Think of ripples in water.",
    options=TF_OPTIONS)

TREE = ("Look at this tree (visit children left to right):\n\n"
        "```\n"
        "A -> B, C\n"
        "B -> D, E\n"
        "C -> F\n"
        "```\n")

add("Problem Solving", "Breadth-First Search", "Hard",
    TREE + "\nIn which order does BFS visit the nodes?",
    "A, B, C, D, E, F",
    "BFS goes level by level: A | B, C | D, E, F.",
    "Level 0, then level 1, then level 2.",
    options=["A, B, C, D, E, F", "A, B, D, E, C, F", "A, C, B, F, E, D", "A, B, D, C, E, F"],
    search=True)

# ============================ DFS ============================
add("MCQ", "Depth-First Search", "Easy",
    "DFS uses which data structure?",
    "Stack",
    "DFS goes deep first, so the last node added is explored first. That is a stack.",
    "Last in, first out.",
    options=["Stack", "Queue", "Table", "Graph paper"])

add("Fill in the Blanks", "Depth-First Search", "Medium",
    "DFS explores one path as ________ as possible before backtracking.",
    "deep",
    "DFS goes deeper and deeper until a dead end, then comes back.",
    "Opposite of 'shallow'.",
    accept=["deep", "deeper", "far"])

add("Problem Solving", "Depth-First Search", "Hard",
    TREE + "\nIn which order does DFS visit the nodes?",
    "A, B, D, E, C, F",
    "DFS goes A -> B -> D, then back to B -> E, then back to A -> C -> F.",
    "Go down the left side first.",
    options=["A, B, D, E, C, F", "A, B, C, D, E, F", "A, C, F, B, D, E", "A, B, D, C, F, E"],
    search=True)

# ============================ ITERATIVE DEEPENING ============================
add("MCQ", "Iterative Deepening", "Easy",
    "Iterative Deepening search repeats DFS with an increasing ________.",
    "Depth limit",
    "It runs DFS with limit 0, then 1, then 2, and so on.",
    "How deep we are allowed to go.",
    options=["Depth limit", "Colour", "Speed", "Memory size"])

add("MCQ", "Iterative Deepening", "Medium",
    "Iterative Deepening combines the good points of...",
    "BFS and DFS",
    "It uses little memory like DFS and finds the shallowest goal like BFS.",
    "Two basic searches.",
    options=["BFS and DFS", "Hill climbing and A*", "CSP and MEA", "Greedy and random"])

add("Scenario", "Iterative Deepening", "Hard",
    "A chess program has only 5 seconds and does not know how deep to search. It searches depth 1, then 2, then 3 and so on, so a good move is always ready. Which search is this?",
    "Iterative deepening",
    "Going deeper step by step means a result for the last completed depth is always available.",
    "Increase the depth one by one.",
    options=["Iterative deepening", "Plain BFS", "Hill climbing", "Random search"],
    real=True)

# ============================ HILL CLIMBING ============================
add("MCQ", "Hill Climbing", "Easy",
    "Hill climbing always moves to a neighbour that is...",
    "Better than the current state",
    "Like climbing a hill, it keeps going up to better states.",
    "Up the hill = better.",
    options=["Better than the current state", "Worse than the current state", "Random", "The same as the current"])

add("Fill in the Blanks", "Hill Climbing", "Medium",
    "When hill climbing reaches a peak that is not the highest peak, it is stuck at a local ________.",
    "maximum",
    "A local maximum is better than its neighbours but not the best overall.",
    "Opposite of minimum.",
    accept=["maximum", "maxima", "peak"])

add("Match the Following", "Hill Climbing", "Medium",
    "Match the hill climbing type with its meaning.",
    "See pairs",
    "Simple takes the first better move, steepest takes the best move, random-restart tries again from new places.",
    "First, best, restart.",
    pairs=[("Simple hill climbing", "Takes the first better neighbour"),
           ("Steepest-ascent", "Checks all neighbours and takes the best"),
           ("Random-restart", "Starts again from a new random place"),
           ("Stochastic", "Picks randomly among the better neighbours")])

add("Problem Solving", "Hill Climbing", "Hard",
    "Current value is 5. Neighbours are 4, 6 and 8 (higher is better). Which value does steepest-ascent hill climbing choose?",
    "8",
    "Steepest-ascent checks all neighbours and chooses the highest, which is 8.",
    "Pick the biggest.",
    options=["8", "6", "4", "5"],
    search=True)

add("True/False", "Hill Climbing", "Easy",
    "Hill climbing can get stuck at a local maximum.",
    "True",
    "At a local maximum no neighbour is better, so hill climbing stops.",
    "Think of a small hill next to a big mountain.",
    options=TF_OPTIONS)

# ============================ HEURISTIC SEARCH ============================
add("MCQ", "Heuristic Search", "Easy",
    "What is a heuristic?",
    "A guess that helps the search move in the right direction",
    "A heuristic is a rule of thumb that estimates how close a state is to the goal.",
    "Think 'smart guess'.",
    options=["A guess that helps the search move in the right direction", "A type of computer",
             "A wrong answer", "A final answer"])

add("Fill in the Blanks", "Heuristic Search", "Medium",
    "h(n) is the estimated cost from node n to the ________.",
    "goal",
    "h(n) estimates the remaining cost to reach the goal.",
    "Where do we want to reach?",
    accept=["goal", "goal state"])

add("Scenario", "Heuristic Search", "Medium",
    "Google Maps estimates the remaining distance to your destination as a straight line. What is this estimate called in AI?",
    "Heuristic",
    "A straight-line distance is a quick estimate of the remaining cost, i.e., a heuristic.",
    "It is an estimate, not the exact road distance.",
    options=["Heuristic", "Goal test", "Constraint", "Production rule"],
    real=True)

add("Problem Solving", "Heuristic Search", "Hard",
    "8-puzzle heuristic 'misplaced tiles' counts the tiles that are not in their goal place.\n\n"
    "```\nCurrent     Goal\n1 2 3       1 2 3\n4 _ 6       4 5 6\n7 5 8       7 8 _\n```\n"
    "How many tiles (not counting the blank) are misplaced?",
    "2",
    "Only tile 5 and tile 8 are in wrong places, so h = 2.",
    "Compare each tile with the goal.",
    options=["2", "1", "3", "4"],
    search=True)

# ============================ BEST-FIRST SEARCH ============================
add("MCQ", "Best-First Search", "Easy",
    "Best-First Search always expands the node that looks...",
    "Most promising (best)",
    "It picks the node with the best (lowest) evaluation value.",
    "The name says it.",
    options=["Most promising (best)", "Oldest", "Largest", "Random"])

add("MCQ", "Best-First Search", "Medium",
    "Greedy best-first search chooses a node using...",
    "Only the heuristic h(n)",
    "Greedy best-first looks only at how close the node seems to be to the goal.",
    "It is greedy for the goal.",
    options=["Only the heuristic h(n)", "Only the cost so far g(n)", "Both g(n) and h(n)", "The depth only"])

add("Fill in the Blanks", "Best-First Search", "Hard",
    "A* search uses f(n) = g(n) + ________.",
    "h(n)",
    "g(n) is the cost so far and h(n) is the estimated cost to the goal.",
    "The heuristic.",
    accept=["h(n)", "h", "h (n)"])

# ============================ CROSS-TOPIC ASSERTION-REASON & MATCH ============================
add("Assertion-Reason", "Depth-First Search", "Medium",
    "Assertion (A): DFS needs less memory than BFS.\n\n"
    "Reason (R): DFS keeps only one path (and a few nodes) in memory, while BFS keeps a whole level.",
    AR_OPTIONS[0],
    "DFS stores only the current path, so memory use is small. BFS stores all nodes of a level, which can be huge.",
    "Compare one path with a whole level.",
    options=AR_OPTIONS)

add("Match the Following", "Breadth-First Search", "Medium",
    "Match the search method with how it works.",
    "See pairs",
    "BFS uses a queue, DFS uses a stack, hill climbing moves to better neighbours, and A* uses g(n) + h(n).",
    "Think of the data structure or the idea.",
    pairs=[("BFS", "Uses a queue and goes level by level"),
           ("DFS", "Uses a stack and goes deep first"),
           ("Hill climbing", "Keeps moving to a better neighbour"),
           ("A*", "Uses cost so far plus estimate to goal")])

# ============================ CSP ============================
add("MCQ", "Constraint Satisfaction Problems", "Easy",
    "A CSP has variables, domains and ________.",
    "Constraints",
    "A CSP is solved by giving each variable a value from its domain without breaking any constraint.",
    "Rules that must not be broken.",
    options=["Constraints", "Heuristics", "Actuators", "Queues"])

add("Scenario", "Constraint Satisfaction Problems", "Medium",
    "In map colouring, neighbouring regions must have different colours. What are the 'variables'?",
    "The regions",
    "Each region is a variable, the colours are the domain, and 'neighbours differ' is the constraint.",
    "What do we need to colour?",
    options=["The regions", "The colours", "The borders", "The pencils"],
    real=True)

add("Scenario", "Constraint Satisfaction Problems", "Medium",
    "A college makes an exam timetable so that two exams with the same students are not on the same day. Which type of problem is this?",
    "Constraint Satisfaction Problem",
    "Exams are variables, days are the domain, and 'no clash' is the constraint.",
    "There is a rule that must not be broken.",
    options=["Constraint Satisfaction Problem", "Turing Test", "Hill climbing only", "Image recognition"],
    real=True)

add("Problem Solving", "Constraint Satisfaction Problems", "Hard",
    "Three regions A, B and C all touch each other. You have 3 colours. A is Red, B is Blue. What colour can C be?",
    "Green",
    "C touches both A (Red) and B (Blue), so it must be the third colour, Green.",
    "C cannot be Red or Blue.",
    options=["Green", "Red", "Blue", "Any colour"],
    search=True)

add("True/False", "Constraint Satisfaction Problems", "Easy",
    "Sudoku can be solved as a Constraint Satisfaction Problem.",
    "True",
    "Cells are variables, numbers 1-9 are the domain, and no repeats in a row, column or box are the constraints.",
    "Sudoku has rules that cannot be broken.",
    options=TF_OPTIONS,
    real=True)

# ============================ MEANS-END ANALYSIS ============================
add("MCQ", "Means-End Analysis", "Easy",
    "Means-End Analysis tries to reduce the ________ between the current state and the goal state.",
    "Difference",
    "MEA finds the difference between where we are and where we want to be, then picks actions to reduce it.",
    "Gap between two states.",
    options=["Difference", "Colour", "Speed", "Size of memory"])

add("MCQ", "Means-End Analysis", "Medium",
    "Which program famously used Means-End Analysis?",
    "General Problem Solver (GPS)",
    "Newell and Simon's General Problem Solver used MEA.",
    "GPS stands for General ...",
    options=["General Problem Solver (GPS)", "Google Maps", "Siri", "Deep Blue"])

add("Scenario", "Means-End Analysis", "Hard",
    "A robot is in Room A and wants to reach Room C. It checks the difference (distance), then chooses the action 'move' to reduce it. Which method is this?",
    "Means-End Analysis",
    "Finding the difference between current and goal state and choosing an action to reduce it is Means-End Analysis.",
    "Reduce the gap step by step.",
    options=["Means-End Analysis", "Turing Test", "Random restart", "Hill climbing only"],
    real=True)
