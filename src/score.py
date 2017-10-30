from functools import total_ordering


@total_ordering
class Score(object):
    """
    The class to represent a score.
    """
    def __init__(self, pseudo: str, score: int) -> None:
        self.pseudo = pseudo
        self.score = score

    def __eq__(self, other: 'Score') -> bool:
        """
        Function to check if two score are equal.
        @param other: the other score to compare with.
        @return: True if they are equal, False otherwise.
        """
        return self.score == other.score

    def __lt__(self, other: 'Score') -> bool:
        """
        Function to check if one score is lower than another.
        @param other: the other score to compare with.
        @return: True if he is lower, False otherwise.
        """
        return self.score < other.score

    def __str__(self) -> str:
        """
        Function to represent a score by a string.
        @return: The string representing the score.
        """
        return self.pseudo + " " + str(self.score) + "\n"


class ScoreManager(object):
    """
    The class to represent the best score.
    This class is a singleton.
    """
    class __ScoreManager:
        def __init__(self) -> None:
            self.best_score_file = "best_score.data"
            self.scores = self.load_score_file()

        def load_score_file(self) -> [Score]:
            try:
                with open(self.best_score_file, "r") as f:
                    scores = [score.strip().split(" ") for score in f]
                    scores = [Score(e[0], int(e[1])) for e in scores]
                    return scores
            except FileNotFoundError:
                return []

    instance = None

    def __init__(self) -> None:
        if not ScoreManager.instance:
            ScoreManager.instance = ScoreManager.__ScoreManager()

    def update_score_file(self) -> None:
        """
        Function to update the score file by adding the new best score.
        """
        with open(self.instance.best_score_file, 'w') as f:
            for score in self.instance.scores:
                f.write(str(score))

    def pos_as_score(self, score: Score) -> int:
        """
        Function to check what would be the position of the given score
        in the best score.
        @param score: The score the user want to check the position.
        @return: The position if this score was to be inserted in the best score.
        """
        i = 0
        for s in self.instance.scores:
            if s > score:
                i += 1
            else:
                return i
        return i

    def add_score(self, score: Score, pos: int) -> None:
        """
        Function to add a score to the best scores.
        @param score: The score to be inserted.
        @param pos: The position where it belongs.
        """
        self.instance.scores.insert(pos, score)
        if len(self.instance.scores) > 10:
            self.instance.scores.pop()
        self.update_score_file()