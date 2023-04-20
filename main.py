from datetime import datetime
from application.salary import calculate_salary
from application.db.people import get_employees
import pygame



time = datetime.now()
print(time)

def main():
    salary = calculate_salary(10, 160)
    print(salary)
    get_employees()

    pygame.init()
    screen = pygame.display.set_mode((400, 300))
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    main()