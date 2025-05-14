import logging
from datetime import datetime
from dotenv import load_dotenv

from helpers import sanity_checks, append_to_review_log
from pipelines import research_step, synthesis_step, tweet_step

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
load_dotenv()


def approval_loop(state):
    errors = sanity_checks(state['final_report'], state['tweets'])
    if errors:
        logger.warning("Automated checks flagged issues: %s", errors)
    print("\n--- Report ---")
    print(state['final_report'][:500] + ('...' if len(state['final_report'])>500 else ''))
    print("\n--- Tweets ---")
    print(state['tweets'])

    decision = input("[A]pprove/[R]equest revisions? ").lower().strip()
    comments = input("Comments: ").replace(',', ';')
    entry = {"timestamp": datetime.utcnow().isoformat(), "decision": decision, "comments": comments}
    append_to_review_log(state['query'], entry)
    return decision == 'a'


if __name__ == '__main__':
    query = input("Enter research query: ")
    while True:
        state = research_step(query)
        print("\nSnippet:", state['research_result'])
        if input("[C]ontinue/[R]e-enter? ").lower().strip()=='c':
            break
        query = input("Re-enter query: ")

    while True:
        state = synthesis_step(state)
        state = tweet_step(state)
        if approval_loop(state):
            break
        print("Re-running generation...")

    print("\n=== Final Report ===\n", state['final_report'])
    print("\n=== Final Tweets ===\n", state['tweets'])
