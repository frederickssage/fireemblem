"""Classes and code related to FireEmblemJobs"""


class FireEmblemJob(object):

    def __init__(self, job_key, ruleset_state):
        self.job_code = job_key
        self.job_name = None
        self.stat_caps = None
        self.job_stat_growths = None
        self.weapon_prof_array = None
        self.media_assets = None
        self.load_self_from_ruleset_state(ruleset_state)

    def load_self_from_ruleset_state(self, ruleset_state):
        pass

