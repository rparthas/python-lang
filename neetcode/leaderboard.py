import heapq

class Leaderboard:
    def __init__(self):
        self.scores = {}


    def print(self):
        print([(id,self.scores[id]) for id in self.scores])

    def addScore(self,id, score):
        self.scores[id] = self.scores.get(id,0)+score
        self.print()

    def top(self,k) ->int:
        sum = 0
        scores = list(self.scores.values())
        heapq.heapify(scores)
        for score in heapq.nlargest(k,scores):
            sum = sum+ score
        return sum

    def reset(self,id):
        self.scores[id] =0
        self.print()

if __name__ == "__main__":
    # Test Case Set 1: Basic Updates and Top K
        print("--- Test Case Set 1 ---")
        lb1 = Leaderboard()
        lb1.addScore(1, 10)
        lb1.addScore(2, 20)
        lb1.addScore(1, 5)    # Update player 1 score to 15
        assert lb1.top(1) == 20, f"Test 1.1 Failed: Expected 20, got {lb1.top(1)}"
        assert lb1.top(2) == 35, f"Test 1.2 Failed: Expected 35, got {lb1.top(2)}"
        lb1.addScore(3, 25)
        assert lb1.top(2) == 45, f"Test 1.3 Failed: Expected 45, got {lb1.top(2)}"
        lb1.reset(3)
        assert lb1.top(2) == 35, f"Test 1.4 Failed: Expected 35, got {lb1.top(2)}"
        print("Test Case Set 1 Passed!")

        # Test Case Set 2: Resetting Top Players and K Edge Cases
        print("\n--- Test Case Set 2 ---")
        lb2 = Leaderboard()
        lb2.addScore(10, 100)
        lb2.addScore(20, 150)
        lb2.addScore(30, 120)
        lb2.addScore(40, 180)
        assert lb2.top(3) == 450, f"Test 2.1 Failed: Expected 450, got {lb2.top(3)}" # 180 + 150 + 120
        lb2.reset(40)          # Reset top player
        assert lb2.top(3) == 370, f"Test 2.2 Failed: Expected 370, got {lb2.top(3)}" # 150 + 120 + 100
        lb2.reset(20)          # Reset another high player
        assert lb2.top(3) == 220, f"Test 2.3 Failed: Expected 220, got {lb2.top(3)}" # 120 + 100 + 0 (player 30, 10, 40/20)

        # K greater than number of players (should sum all existing scores)
        assert lb2.top(5) == 220, f"Test 2.4 Failed: Expected 220, got {lb2.top(5)}" # 120 + 100 + 0 + 0
        # K = 0
        assert lb2.top(0) == 0,   f"Test 2.5 Failed: Expected 0, got {lb2.top(0)}"
        print("Test Case Set 2 Passed!")

        # Test Case Set 3: Players with Same Scores
        print("\n--- Test Case Set 3 ---")
        lb3 = Leaderboard()
        lb3.addScore(1, 50)
        lb3.addScore(2, 60)
        lb3.addScore(3, 50) # Same score as player 1
        lb3.addScore(4, 60) # Same score as player 2
        lb3.addScore(5, 55)
        assert lb3.top(1) == 60,  f"Test 3.1 Failed: Expected 60, got {lb3.top(1)}"
        assert lb3.top(2) == 120, f"Test 3.2 Failed: Expected 120, got {lb3.top(2)}" # 60 + 60
        assert lb3.top(3) == 175, f"Test 3.3 Failed: Expected 175, got {lb3.top(3)}" # 60 + 60 + 55
        assert lb3.top(4) == 225, f"Test 3.4 Failed: Expected 225, got {lb3.top(4)}" # 60 + 60 + 55 + 50
        assert lb3.top(5) == 275, f"Test 3.5 Failed: Expected 275, got {lb3.top(5)}" # 60 + 60 + 55 + 50 + 50
        lb3.reset(2) # Reset one of the 60s
        lb3.reset(4) # Reset the other 60
        assert lb3.top(3) == 155, f"Test 3.6 Failed: Expected 105, got {lb3.top(3)}" # 55 + 50 + 50
        print("Test Case Set 3 Passed!")

        # Test Case Set 4: Empty Leaderboard and Adding Back
        print("\n--- Test Case Set 4 ---")
        lb4 = Leaderboard()
        assert lb4.top(1) == 0, f"Test 4.1 Failed: Expected 0, got {lb4.top(1)}" # Empty board
        lb4.addScore(1, 10)
        lb4.addScore(2, 20)
        assert lb4.top(1) == 20, f"Test 4.2 Failed: Expected 20, got {lb4.top(1)}"
        lb4.reset(1)
        lb4.reset(2)
        assert lb4.top(1) == 0, f"Test 4.3 Failed: Expected 0, got {lb4.top(1)}" # All reset to 0
        assert lb4.top(2) == 0, f"Test 4.4 Failed: Expected 0, got {lb4.top(2)}" # All reset to 0
        lb4.addScore(1, 30) # Add back player 1
        assert lb4.top(1) == 30, f"Test 4.5 Failed: Expected 30, got {lb4.top(1)}"
        assert lb4.top(2) == 30, f"Test 4.6 Failed: Expected 30, got {lb4.top(2)}" # 30 + 0
        print("Test Case Set 4 Passed!")

        # Test Case Set 5: Original Example from Prompt
        print("\n--- Test Case Set 5 (Original Example) ---")
        leaderboard = Leaderboard ()
        leaderboard.addScore(1,73)
        leaderboard.addScore(2,56)
        leaderboard.addScore(3,39)
        leaderboard.addScore(4,51)
        leaderboard.addScore(5,4)
        assert leaderboard.top(1) == 73, f"Test 5.1 Failed: Expected 73, got {leaderboard.top(1)}"
        leaderboard.reset(1)
        leaderboard.reset(2)
        leaderboard.addScore(2,51) # Player 2 score becomes 0 + 51 = 51
        # Current scores: {3: 39, 4: 51, 5: 4, 1: 0, 2: 51}
        # Top 3 scores are: 51 (p4), 51 (p2), 39 (p3)
        assert leaderboard.top(3) == 141, f"Test 5.2 Failed: Expected 141, got {leaderboard.top(3)}" # 51 + 51 + 39
        print("Test Case Set 5 Passed!")


        print("\n-------------------------")
        print("All test cases passed!")
        print("-------------------------")
