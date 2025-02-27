# import warnings

# from crew import CrewZaai
# from dotenv import load_dotenv


# warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")
# load_dotenv()


# def run():
#     """Run the crew."""

#     inputs = {"topic": "AI Agents"}
#     CrewZaai().crew().kickoff(inputs=inputs)


# if __name__ == "__main__":
#     run()


### with command line arguments
import warnings
import argparse
from crew import CrewZaai
from dotenv import load_dotenv

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")
load_dotenv()

def run(topic):
    """Run the crew."""
    inputs = {"topic": topic}
    CrewZaai().crew().kickoff(inputs=inputs)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Run the CrewZaai with a specific topic.')
    parser.add_argument('topic', type=str, help='The topic for the CrewZaai')
    args = parser.parse_args()
    run(args.topic)

