# Pong Game (Python)

A classic Pong clone built with Python's built-in `turtle` graphics module, made as a learning project to practice object-oriented programming, game loops, and debugging real gameplay bugs.

## What This Is

Two paddles, one ball, first to rack up points wins. Built from scratch to get hands-on practice with:

- Object-oriented design (`Ball`, `Paddle`, and `ScoreBoard` as classes inheriting from `Turtle`)
- Game loops and frame-based movement
- Collision detection
- Keyboard input handling
- Debugging logic errors that only show up when you actually play the game, not just read the code

## How to Run

Requires Python 3 (the `turtle` module is part of the standard library, no installs needed).

```bash
python main.py
```

## Controls

| Player | Up | Down |
|---|---|---|
| Left paddle | `W` | `S` |
| Right paddle | `↑` | `↓` |

First to miss the ball gives the other player a point. The scoreboard displays at the top of the screen.

## Project Structure

```
├── main.py         # Game loop, window setup, collision/scoring logic
├── ball.py         # Ball class: movement, bouncing, speed, reset behavior
├── paddle.py        # Paddle class: movement and boundary handling
└── scoreboard.py     # ScoreBoard class: tracking and displaying points
```

## Bugs Found & Fixed During Development

Part of the learning value here was in what went wrong before it worked correctly:

- **Ball tunneling through paddles** — the original collision check used an open-ended distance/position condition that stayed `True` indefinitely once the ball crossed the paddle's front edge, letting the ball "pass through" and bounce off the *back* of the paddle instead. Fixed by bounding the collision zone to a narrow strip right at the paddle's edge, and checking the ball's direction of travel so it can't re-trigger.
- **Paddles moving off-screen** — paddle movement had no boundary check, so holding a key long enough pushed the paddle past the top or bottom of the window. Fixed by clamping the paddle's y-position to the playable window height before allowing movement.

## What I'd Improve Next

- Add a max-score win condition and a "Game Over" screen
- Add a proper hitbox check based on paddle shape rather than a fixed-width strip, so collisions stay accurate if paddle size changes
- Add unit tests for the `Ball` and `Paddle` classes independent of the turtle graphics loop

## Built With

- Python 3
- [turtle](https://docs.python.org/3/library/turtle.html) — standard library graphics module
