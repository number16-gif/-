import random


def get_computer_choice():
    """Компьютер случайно выбирает вариант."""
    choices = ['Камень', 'Ножницы', 'Бумага']
    return random.choice(choices)


def get_player_choice():
    """Получает выбор игрока."""
    print("\nВыберите:")
    print("  1 - Камень")
    print("  2 - Ножницы")
    print("  3 - Бумага")
    print("  0 - Выйти из игры")
    
    choice = input("Ваш выбор: ").strip()
    
    if choice == '0':
        return None
    
    if choice == '1':
        return 'Камень'
    elif choice == '2':
        return 'Ножницы'
    elif choice == '3':
        return 'Бумага'
    else:
        print("Ошибка: неверный выбор! Попробуйте снова.")
        return get_player_choice()


def determine_winner(player, computer):
    """
    Определяет победителя раунда.
    
    Возвращает:
        'player' - победил игрок
        'computer' - победил компьютер
        'draw' - ничья
    """
    if player == computer:
        return 'draw'
    elif (player == 'Камень' and computer == 'Ножницы') or \
         (player == 'Ножницы' and computer == 'Бумага') or \
         (player == 'Бумага' and computer == 'Камень'):
        return 'player'
    else:
        return 'computer'


def play_game():
    """Запускает игру."""
    player_score = 0
    computer_score = 0
    rounds_played = 0
    wins = 0
    losses = 0
    draws = 0
    
    print("\n" + "="*50)
    print("ИГРА 'КАМЕНЬ, НОЖНИЦЫ, БУМАГА'")
    print("="*50)
    print("\nПравила:")
    print("  Камень побеждает Ножницы")
    print("  Ножницы побеждают Бумагу")
    print("  Бумага побеждает Камень")
    print("\nЦель: первым набрать 3 очка")
    print("Для выхода введите 0\n")
    print("="*50)
    
    while True:
        # Сбрасываем счет для новой игры
        player_score = 0
        computer_score = 0
        rounds_played = 0
        
        print("\n--- НОВАЯ ИГРА ---")
        print(f"Счет: Вы {player_score} : {computer_score} Компьютер")
        
        # Играем до 3 побед
        while player_score < 3 and computer_score < 3:
            # Получаем выбор игрока
            player_choice = get_player_choice()
            if player_choice is None:
                print("\nДо свидания!")
                return
            
            # Компьютер делает выбор
            computer_choice = get_computer_choice()
            
            print(f"\nВы выбрали: {player_choice}")
            print(f"Компьютер выбрал: {computer_choice}")
            
            # Определяем победителя
            winner = determine_winner(player_choice, computer_choice)
            rounds_played += 1
            
            if winner == 'player':
                player_score += 1
                wins += 1
                print("[+] Вы выиграли этот раунд!")
            elif winner == 'computer':
                computer_score += 1
                losses += 1
                print("[-] Компьютер выиграл этот раунд!")
            else:
                draws += 1
                print("[=] Ничья!")
            
            # Показываем текущий счет
            print(f"\nСчет: Вы {player_score} : {computer_score} Компьютер")
        
        # Определяем победителя игры
        print("\n" + "="*40)
        if player_score > computer_score:
            print("[ПОБЕДА] ПОЗДРАВЛЯЮ! ВЫ ВЫИГРАЛИ ИГРУ!")
        else:
            print("[ПОРАЖЕНИЕ] КОМПЬЮТЕР ВЫИГРАЛ ИГРУ")
        print("="*40)
        
        # Показываем статистику
        print("\n" + "="*40)
        print("СТАТИСТИКА ИГР")
        print("="*40)
        print(f"Всего игр: {wins + losses + draws}")
        print(f"Побед: {wins}")
        print(f"Поражений: {losses}")
        print(f"Ничьих: {draws}")
        
        total = wins + losses + draws
        if total > 0:
            win_rate = (wins / total) * 100
            print(f"Процент побед: {win_rate:.1f}%")
        print("="*40)
        
        # Спрашиваем, хочет ли игрок продолжить
        again = input("\nХотите сыграть еще? (да/нет): ").strip().lower()
        if again not in ('да', 'lf', 'yes', 'y', 'д'):
            print("\nСпасибо за игру! До встречи!")
            break
        else:
            print("\nОтлично! Начинаем новую игру!")


if __name__ == "__main__":
    play_game()
