"""
AI Quiz Arena - DSC401-6 Artificial Intelligence (Units I & II)
Interactive quiz game built with Streamlit.

Features: difficulty levels, topic filter, random questions, per-question timer,
progress bar, immediate feedback with explanations, lifelines (50-50, Hint, Skip),
streak bonus, final report with topic analysis, leaderboard, CSV download.

Run:  streamlit run app.py
"""
import copy
import datetime
import json
import os
import random
import time

import pandas as pd
import streamlit as st



# ============================ QUESTION BANK ============================


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


st.set_page_config(page_title="AI Quiz Arena", page_icon="🤖", layout="centered")


# ----------------------------------------------------------------------------
# Colourful theme
# ----------------------------------------------------------------------------
THEME_CSS = """
<style>
.stApp {background: linear-gradient(135deg, #ede7ff 0%, #e0f2ff 45%, #e6fff4 100%);}
[data-testid="stHeader"] {background: transparent;}
[data-testid="stSidebar"] {background: linear-gradient(180deg, #4f46e5 0%, #7c3aed 100%);}
[data-testid="stSidebar"] * {color: #ffffff !important;}
[data-testid="stSidebar"] [data-testid="stMetricValue"] {color: #fde047 !important;}
[data-testid="stSidebar"] [data-testid="stMetric"] {background: rgba(255,255,255,.18);
        border-left: 6px solid #fde047; box-shadow: none;}
[data-testid="stSidebar"] [data-testid="stMetricLabel"] * {color: #ffffff !important;}
.hero {background: linear-gradient(90deg, #4f46e5, #7c3aed, #ec4899); color: white;
       padding: 28px 24px; border-radius: 18px; text-align: center;
       box-shadow: 0 8px 20px rgba(79,70,229,.35); margin-bottom: 18px;}
.hero h1 {color: white !important; margin: 0; font-size: 2.2rem;}
.hero p {color: #f5f3ff; margin: 6px 0 0 0; font-size: 1rem;}
.badge {display: inline-block; padding: 4px 12px; margin: 0 6px 8px 0; border-radius: 999px;
        font-size: .8rem; font-weight: 700; color: white;}
.b-easy {background: #16a34a;} .b-medium {background: #f59e0b;} .b-hard {background: #dc2626;}
.b-topic {background: #4f46e5;} .b-type {background: #0891b2;}
[data-testid="stVerticalBlockBorderWrapper"] {background: rgba(255,255,255,.85);
        border-radius: 16px; border: 2px solid #c7d2fe;}
div.stButton > button {border-radius: 12px; font-weight: 700; border: none; color: white;
        background: linear-gradient(90deg, #6366f1, #8b5cf6); box-shadow: 0 3px 8px rgba(99,102,241,.35);}
div.stButton > button:hover {transform: translateY(-1px); color: white;
        background: linear-gradient(90deg, #4f46e5, #7c3aed);}
div.stButton > button:disabled {background: #cbd5e1; color: #64748b; box-shadow: none;}
div.stButton > button[kind="primary"] {background: linear-gradient(90deg, #10b981, #059669);}
[data-testid="stMetric"] {background: white; padding: 12px; border-radius: 14px;
        border-left: 6px solid #8b5cf6; box-shadow: 0 2px 8px rgba(0,0,0,.08);}
.stProgress > div > div > div > div {background: linear-gradient(90deg, #06b6d4, #8b5cf6, #ec4899);}
h1, h2, h3 {color: #312e81;}
</style>
"""
st.markdown(THEME_CSS, unsafe_allow_html=True)


def hero(title, subtitle):
    st.markdown(f'<div class="hero"><h1>{title}</h1><p>{subtitle}</p></div>',
                unsafe_allow_html=True)

# ----------------------------------------------------------------------------
# Constants
# ----------------------------------------------------------------------------
LB_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "leaderboard.json")
BASE_POINTS = {"Easy": 10, "Medium": 15, "Hard": 20}
HINT_COST, FIFTY_COST, STREAK_BONUS, MIN_POINTS = 3, 5, 5, 2
TOPICS = sorted({q["topic"] for q in QUESTIONS})
PLACEHOLDER = "-- choose --"
LEVEL_ICON = {"Easy": "🟢", "Medium": "🟡", "Hard": "🔴"}

# ----------------------------------------------------------------------------
# Leaderboard (JSON file; falls back to session if the file system is read-only)
# ----------------------------------------------------------------------------
def load_leaderboard():
    try:
        with open(LB_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return st.session_state.get("_lb_fallback", [])


def save_leaderboard(entries):
    st.session_state["_lb_fallback"] = entries
    try:
        with open(LB_FILE, "w", encoding="utf-8") as f:
            json.dump(entries, f, indent=2)
    except Exception:
        pass


# ----------------------------------------------------------------------------
# Session state
# ----------------------------------------------------------------------------
def reset_game():
    keep = {k: st.session_state[k] for k in ("_lb_fallback",) if k in st.session_state}
    st.session_state.clear()
    st.session_state.update(keep)
    st.session_state.update(
        stage="start", qs=[], i=0, score=0, streak=0, best_streak=0, correct=0,
        results=[], phase="answering", started=0.0, timer=30,
        hints_left=3, fifty_left=2, skip_left=1,
        hint_used=False, fifty_used=False, removed=[], name="Player",
        level="All", lb_saved=False, last=None,
    )


if "stage" not in st.session_state:
    reset_game()

S = st.session_state


# ----------------------------------------------------------------------------
# Game logic
# ----------------------------------------------------------------------------
def build_quiz(name, level, n, timer, topics, shuffle_q):
    pool = [q for q in QUESTIONS
            if (level == "All" or q["level"] == level) and q["topic"] in topics]
    if shuffle_q:
        random.shuffle(pool)
    pool = pool[:n]
    quiz = []
    for q in pool:
        q = copy.deepcopy(q)
        if q["type"] in ("MCQ", "Scenario", "Problem Solving"):
            q["opts"] = random.sample(q["options"], len(q["options"]))
        elif q.get("options"):
            q["opts"] = list(q["options"])      # True/False & Assertion-Reason keep fixed order
        if q["type"] == "Match the Following":
            q["rights"] = random.sample([r for _, r in q["pairs"]], len(q["pairs"]))
        quiz.append(q)
    S.update(stage="quiz", qs=quiz, i=0, score=0, streak=0, best_streak=0, correct=0,
             results=[], phase="answering", timer=timer, name=name or "Player",
             level=level, hints_left=3, fifty_left=2, skip_left=1, lb_saved=False,
             last=None)
    start_question()


def start_question():
    S.phase = "answering"
    S.started = time.time()
    S.hint_used = False
    S.fifty_used = False
    S.removed = []


def current():
    return S.qs[S.i]


def collect_answer(q):
    """Read the user's current answer from widget state."""
    i = S.i
    if q["type"] == "Fill in the Blanks":
        return (S.get(f"ans_{i}") or "").strip()
    if q["type"] == "Match the Following":
        ans = {}
        for j, (left, _) in enumerate(q["pairs"]):
            ans[left] = S.get(f"m_{i}_{j}", PLACEHOLDER)
        return ans
    return S.get(f"ans_{i}")


def is_answered(q, ans):
    if q["type"] == "Match the Following":
        return all(v != PLACEHOLDER for v in ans.values())
    return bool(ans)


def check(q, ans):
    if q["type"] == "Fill in the Blanks":
        return ans.strip().lower() in [a.lower() for a in q["accept"]]
    if q["type"] == "Match the Following":
        return all(dict(q["pairs"])[left] == right for left, right in ans.items())
    return ans == q["answer"]


def remaining_time():
    if not S.timer:
        return None
    return S.timer - (time.time() - S.started)


def resolve(ans=None, timeout=False):
    q = current()
    rem = remaining_time()
    correct = False if timeout or ans is None else check(q, ans)
    pts, detail = 0, []
    if correct:
        base = BASE_POINTS[q["level"]]
        pts = base
        detail.append(f"Base ({q['level']}): +{base}")
        if S.hint_used:
            pts -= HINT_COST
            detail.append(f"Hint used: -{HINT_COST}")
        if S.fifty_used:
            pts -= FIFTY_COST
            detail.append(f"50-50 used: -{FIFTY_COST}")
        pts = max(pts, MIN_POINTS)
        if rem is not None and rem > 0:
            tb = int(rem // 10)
            if tb:
                pts += tb
                detail.append(f"Speed bonus: +{tb}")
        S.streak += 1
        S.best_streak = max(S.best_streak, S.streak)
        if S.streak >= 3:
            pts += STREAK_BONUS
            detail.append(f"Streak x{S.streak}: +{STREAK_BONUS}")
        S.correct += 1
    else:
        S.streak = 0
    S.score += pts
    S.results.append(dict(
        no=S.i + 1, topic=q["topic"], level=q["level"], type=q["type"], q=q["q"],
        correct=correct, timeout=timeout, skipped=False, points=pts,
        answer=q["answer"], exp=q["exp"],
    ))
    S.last = dict(correct=correct, timeout=timeout, points=pts, detail=detail)
    S.phase = "feedback"


def go_next():
    if S.i + 1 >= len(S.qs):
        S.stage = "result"
    else:
        S.i += 1
        start_question()


def use_hint():
    if S.hints_left > 0 and not S.hint_used:
        S.hints_left -= 1
        S.hint_used = True


def use_fifty():
    q = current()
    if S.fifty_left > 0 and not S.fifty_used and q.get("opts") and len(q["opts"]) > 2:
        wrong = [o for o in q["opts"] if o != q["answer"]]
        S.removed = random.sample(wrong, 2)
        S.fifty_left -= 1
        S.fifty_used = True


def use_skip():
    if S.skip_left > 0:
        S.skip_left -= 1
        q = current()
        S.results.append(dict(
            no=S.i + 1, topic=q["topic"], level=q["level"], type=q["type"], q=q["q"],
            correct=False, timeout=False, skipped=True, points=0,
            answer=q["answer"], exp=q["exp"],
        ))
        S.streak = 0
        go_next()


# ----------------------------------------------------------------------------
# UI pieces
# ----------------------------------------------------------------------------
def start_screen():
    hero("🤖 AI Quiz Arena", "DSC401-6 Artificial Intelligence · Units I & II")
    st.markdown(
        "Test your knowledge of **agents, search, heuristics, CSPs and more**. "
        "Earn points for correct answers, speed and streaks - but lifelines cost points!"
    )

    name = st.text_input("Your name", value=S.name if S.name != "Player" else "")
    c1, c2 = st.columns(2)
    level = c1.selectbox("Difficulty level", ["All", "Easy", "Medium", "Hard"])
    timer = c2.selectbox("Time per question", [30, 45, 60, 90, 0],
                         format_func=lambda x: "No timer" if x == 0 else f"{x} seconds")
    topics = st.multiselect("Topics", TOPICS, default=TOPICS)
    pool_size = len([q for q in QUESTIONS
                     if (level == "All" or q["level"] == level) and q["topic"] in topics])
    if pool_size == 0:
        st.warning("No questions match this selection. Choose more topics or another level.")
        return
    options = sorted({min(n, pool_size) for n in (10, 20, 30, 50, pool_size)})
    n = st.select_slider("Number of questions", options=options, value=min(10, pool_size))
    shuffle_q = st.checkbox("Randomise question order", value=True)

    with st.expander("📜 Rules, scoring & lifelines"):
        st.markdown(
            f"""
- **Points:** Easy {BASE_POINTS['Easy']} · Medium {BASE_POINTS['Medium']} · Hard {BASE_POINTS['Hard']}
- **Speed bonus:** +1 point for every 10 seconds left when you answer correctly
- **Streak bonus:** +{STREAK_BONUS} points from the 3rd correct answer in a row
- **Lifelines:** 💡 Hint ×3 (−{HINT_COST} pts) · ✂️ 50-50 ×2 (−{FIFTY_COST} pts, choice questions only) · ⏭️ Skip ×1 (no points)
- When time runs out the question is marked wrong.
- Final score is saved to the **leaderboard**.
            """
        )
    st.info(f"Question bank: **{len(QUESTIONS)}** questions across **{len(TOPICS)}** topics.")
    if st.button("🚀 Start Quiz", type="primary", width="stretch"):
        build_quiz(name.strip(), level, n, timer, topics, shuffle_q)
        st.rerun()

    show_leaderboard(compact=True)


def sidebar_panel():
    with st.sidebar:
        st.header(f"👤 {S.name}")
        st.metric("Score", S.score)
        c1, c2 = st.columns(2)
        c1.metric("Correct", f"{S.correct}/{len(S.results)}")
        c2.metric("Streak 🔥", S.streak)
        st.divider()
        st.subheader("Lifelines")
        st.write(f"💡 Hints left: **{S.hints_left}**")
        st.write(f"✂️ 50-50 left: **{S.fifty_left}**")
        st.write(f"⏭️ Skips left: **{S.skip_left}**")
        st.divider()
        if st.button("🔄 Quit & restart"):
            reset_game()
            st.rerun()


@st.fragment(run_every=1)
def timer_box():
    """Countdown that refreshes every second without re-running the whole app."""
    if S.stage != "quiz" or S.phase != "answering" or not S.timer:
        return
    rem = remaining_time()
    if rem <= 0:
        resolve(ans=None, timeout=True)
        st.rerun()
    ratio = max(0.0, min(1.0, rem / S.timer))
    st.progress(ratio, text=f"⏱️ {int(rem)} s left")


def answer_widgets(q):
    i = S.i
    t = q["type"]
    if t == "Fill in the Blanks":
        st.text_input("Type your answer", key=f"ans_{i}")
    elif t == "Match the Following":
        for j, (left, _) in enumerate(q["pairs"]):
            st.selectbox(f"**{left}**", [PLACEHOLDER] + q["rights"], key=f"m_{i}_{j}")
    else:
        opts = [o for o in q["opts"] if o not in S.removed]
        if t == "Assertion-Reason":
            st.radio("Choose the correct option", opts, index=None, key=f"ans_{i}")
        else:
            st.radio("Choose one", opts, index=None, key=f"ans_{i}")


def quiz_screen():
    sidebar_panel()
    q = current()
    total = len(S.qs)
    st.progress(S.i / total, text=f"Question {S.i + 1} of {total}")
    st.markdown(
        f'<span class="badge b-{q["level"].lower()}">{q["level"]}</span>'
        f'<span class="badge b-topic">📚 {q["topic"]}</span>'
        f'<span class="badge b-type">🧩 {q["type"]}</span>',
        unsafe_allow_html=True)

    if S.phase == "answering":
        timer_box()
    with st.container(border=True):
        st.markdown(f"### {q['q']}" if "\n" not in q["q"] and "```" not in q["q"] else q["q"])

    if S.phase == "answering":
        if S.hint_used:
            st.info(f"💡 **Hint:** {q['hint']}")
        with st.container(border=True):
            answer_widgets(q)

        c1, c2, c3, c4 = st.columns([2, 1.2, 1.2, 1.2])
        if c1.button("✅ Submit answer", type="primary", width="stretch"):
            ans = collect_answer(q)
            if not is_answered(q, ans):
                st.warning("Please answer before submitting.")
            else:
                resolve(ans)
                st.rerun()
        c2.button("💡 Hint", on_click=use_hint, disabled=S.hints_left == 0 or S.hint_used,
                  width="stretch")
        can_fifty = (S.fifty_left > 0 and not S.fifty_used
                     and bool(q.get("opts")) and len(q["opts"]) > 2)
        c3.button("✂️ 50-50", on_click=use_fifty, disabled=not can_fifty,
                  width="stretch")
        c4.button("⏭️ Skip", on_click=use_skip, disabled=S.skip_left == 0,
                  width="stretch")
    else:
        feedback_view(q)


def feedback_view(q):
    last = S.last
    if last["timeout"]:
        st.error("⏰ Time's up!")
    elif last["correct"]:
        st.success(f"✅ Correct!  +{last['points']} points")
        if last["detail"]:
            st.caption(" · ".join(last["detail"]))
    else:
        st.error("❌ Incorrect")

    if q["type"] == "Match the Following":
        st.markdown("**Correct matches:**")
        for left, right in q["pairs"]:
            st.markdown(f"- **{left}** → {right}")
    else:
        st.markdown(f"**Correct answer:** {q['answer']}")
    st.info(f"📖 **Explanation:** {q['exp']}")

    label = "🏁 Finish quiz" if S.i + 1 >= len(S.qs) else "➡️ Next question"
    if st.button(label, type="primary", width="stretch"):
        go_next()
        st.rerun()


def rank_title(acc):
    if acc >= 90:
        return "🏆 AI Grandmaster"
    if acc >= 75:
        return "🥇 Search Strategist"
    if acc >= 50:
        return "🥈 Rational Agent"
    return "🥉 Learning Agent - keep training!"


def show_leaderboard(compact=False):
    entries = sorted(load_leaderboard(), key=lambda e: (-e["score"], -e["accuracy"]))
    if not entries:
        return
    st.subheader("🏅 Leaderboard")
    df = pd.DataFrame(entries[:10 if not compact else 5])
    df.index = range(1, len(df) + 1)
    df = df[["name", "score", "correct", "total", "accuracy", "level", "date"]]
    df.columns = ["Player", "Score", "Correct", "Questions", "Accuracy %", "Level", "Date"]
    st.dataframe(df, width="stretch")


def result_screen():
    sidebar_panel()
    total = len(S.qs)
    answered = len(S.results)
    acc = round(100 * S.correct / total, 1) if total else 0
    hero("🎉 Quiz complete!", rank_title(acc))
    if acc >= 75 and not S.get("_balloons"):
        st.balloons()
        S["_balloons"] = True

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Final score", S.score)
    c2.metric("Correct", f"{S.correct}/{total}")
    c3.metric("Accuracy", f"{acc}%")
    c4.metric("Best streak", S.best_streak)

    if not S.lb_saved:
        entries = load_leaderboard()
        entries.append(dict(name=S.name, score=S.score, correct=S.correct, total=total,
                            accuracy=acc, level=S.level,
                            date=datetime.date.today().isoformat()))
        save_leaderboard(entries)
        S.lb_saved = True

    df = pd.DataFrame(S.results)
    st.subheader("📊 Topic-wise performance")
    topic_df = (df.groupby("topic")["correct"].agg(["sum", "count"]).reset_index())
    topic_df["Accuracy %"] = (100 * topic_df["sum"] / topic_df["count"]).round(0)
    topic_df.columns = ["Topic", "Correct", "Attempted", "Accuracy %"]
    st.bar_chart(topic_df.set_index("Topic")["Accuracy %"])
    weak = topic_df[topic_df["Accuracy %"] < 60]["Topic"].tolist()
    if weak:
        st.warning("📌 Revise these topics: " + ", ".join(weak))
    else:
        st.success("Great coverage - no weak topics detected!")

    wrong = [r for r in S.results if not r["correct"]]
    if wrong:
        with st.expander(f"🔍 Review {len(wrong)} question(s) you missed or skipped"):
            for r in wrong:
                tag = "⏭️ skipped" if r["skipped"] else ("⏰ timed out" if r["timeout"] else "❌ wrong")
                st.markdown(f"**Q{r['no']}. {r['q']}**  \n_{r['topic']} · {tag}_")
                if r["type"] == "Match the Following":
                    st.markdown("Correct: see the question bank for the pairs.")
                else:
                    st.markdown(f"**Answer:** {r['answer']}")
                st.caption(r["exp"])
                st.divider()

    csv = df.drop(columns=["q", "exp"]).to_csv(index=False).encode("utf-8")
    st.download_button("⬇️ Download my result (CSV)", csv, file_name="ai_quiz_result.csv",
                       mime="text/csv")
    show_leaderboard()
    if st.button("🔁 Play again", type="primary", width="stretch"):
        reset_game()
        st.rerun()


# ----------------------------------------------------------------------------
# Router
# ----------------------------------------------------------------------------
if S.stage == "start":
    start_screen()
elif S.stage == "quiz":
    quiz_screen()
else:
    result_screen()
