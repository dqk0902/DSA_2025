from collections import defaultdict

class Contest:
    def __init__(self, names, task_count):
        self.contestants = {name: [0] * task_count for name in names}
        self.task_count = task_count
        self.total_scores = {name: 0 for name in names}
        self.last_update = {name: float('-inf') for name in names}
        self.submission_count = 0

    def add_submission(self, name, task, score):
        self.submission_count += 1
        task_index = task - 1
        if score > self.contestants[name][task_index]:
            old_score = self.contestants[name][task_index]
            self.contestants[name][task_index] = score
            self.total_scores[name] += score - old_score
            self.last_update[name] = self.submission_count

    def create_scoreboard(self):
        sorted_contestants = sorted(
            self.total_scores.items(),
            key=lambda x: (-x[1], self.last_update[x[0]], x[0])
        )
        
        zero_scores = []
        non_zero_scores = []

        for name, score in sorted_contestants:
            if score == 0:
                zero_scores.append((name, 0))
            else:
                non_zero_scores.append((name, score))

        zero_scores.sort(key=lambda x: x[0])    
        
        return non_zero_scores + zero_scores

if __name__ == "__main__":
    names = ["anna", "pekka", "kalle", "tiina", "eeva"]
    contest = Contest(names, 3)

    contest.add_submission("tiina", 2, 30)
    contest.add_submission("pekka", 1, 40)
    contest.add_submission("tiina", 1, 20)
    contest.add_submission("pekka", 1, 50)
    contest.add_submission("pekka", 2, 0)
    contest.add_submission("eeva", 3, 100)
    contest.add_submission("anna", 1, 0)
    contest.add_submission("eeva", 3, 80)
    contest.add_submission("tiina", 2, 30)

    scoreboard = contest.create_scoreboard()
    print(scoreboard)
    # [('eeva', 100), ('tiina', 50), ('pekka', 50), ('anna', 0), ('kalle', 0)]