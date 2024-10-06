from agents.base_agent import Agent

class ImplementationAgent(Agent):
    def __init__(self, name, client, prompt="", gen_kwargs=None):
        super().__init__(name, client, prompt, gen_kwargs)

    async def execute(self, message_history):
        # Override the execute method if needed
        return await super().execute(message_history)

    def _build_system_prompt(self):
        # Override the _build_system_prompt method if needed
        return super()._build_system_prompt()
