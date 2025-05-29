# modules/validator.py

class ValidatorEngine:
    def __init__(self, idea):
        self.idea = idea

    def score_viability(self):
        score = 0
        if len(self.idea.problem) > 20:
            score += 25
        if len(self.idea.solution) > 20:
            score += 25
        if len(self.idea.audience) > 15:
            score += 25
        if len(self.idea.revenue_model) > 10:
            score += 25
        return score

    def generate_feedback(self):
        score = self.score_viability()
        if score >= 75:
            return f"✅ Your idea '{self.idea.title}' has strong potential. Score: {score}%"
        else:
            return f"⚠️ Your idea '{self.idea.title}' needs more clarity and depth. Score: {score}%"
