def adventureStory(direction):
    if direction == "up":      
        story_1 = input("""You go up the stairs and are startled by a black cat as it jumps from the top of the stair
You fall down the stairs and notice a secret door opened from the wall.
Do you [run] or [enter] the secret wall.""")
        if story_1 == "run": 
            print("""You quickly run out the door, but in your panic you run straight into a bear.
Game Over.""")
    elif direction == "down":
        story_1 = "sadasd"
    return story_1
def main():
    print("""Welcome to the Adventure Story!
By: Lyle Osburne""")
    direction = input("""You got split up from your friend while camping in the woods.
while searching you come across a cabin and you think you saw him inside threw the window.
As you enter the house you see 2 sets of stairs, what do you do?
Do you want to go [up] or [down]:""")
    story_1 = adventureStory(direction)
    print(story_1)
if __name__ == "__main__":
    main()