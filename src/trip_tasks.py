from crewai import Task
from datetime import date
from prompts import IDENTIFY_TASK_PROMPT, GATHER_TASK_PROMPT, PLAN_TASK_PROMPT

class TripTasks:
    def identify_task(self, agent, origin, cities, interests, range):
        return Task(
            description=IDENTIFY_TASK_PROMPT.format(
                origin=origin,
                cities=cities,
                range=range,
                interests=interests,
                tip_section=self.__tip_section(),
            ),
            agent=agent,
            expected_output="A list of recommended destinations based on the criteria.",
            input_type="text",
            output_type="list"
        )

    def gather_task(self, agent, origin, interests, range):
        return Task(
            description=GATHER_TASK_PROMPT.format(
                origin=origin,
                range=range,
                interests=interests,
                tip_section=self.__tip_section(),
            ),
            agent=agent,
            expected_output="Detailed information about activities and attractions.",
            input_type="text",
            output_type="report"
        )

    def plan_task(self, agent, origin, interests, range):
        return Task(
            description=PLAN_TASK_PROMPT.format(
                origin=origin,
                range=range,
                interests=interests,
                tip_section=self.__tip_section(),
            ),
            agent=agent,
            expected_output="A comprehensive travel plan with itinerary and logistics.",
            input_type="text",
            output_type="plan"
        )

    def __tip_section(self):
        return "If you do your BEST WORK, I'll tip you $100!"
