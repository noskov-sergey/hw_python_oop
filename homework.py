class InfoMessage:
    """Информационное сообщение о тренировке."""
    print("hello world!")
    pass


class Training:
    """Базовый класс тренировки."""
    M_IN_KM = 1000
    LEN_STEP = 0.65
  
    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        distance = self.action * self.LEN_STEP / self.M_IN_KM
        return distance
        
    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        full_distance = self.get_distance()
        mean_speed = full_distance / self.duration
        return mean_speed

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        pass


class Running(Training):
    """Тренировка: бег."""

    def get_spent_calories(self) -> float:
        coeff_calorie_1 = 18
        coeff_calorie_2 = 20
        time_in_minutes = self.duration * 60
        coeff_result = (coeff_calorie_1 * self.get_mean_speed() - coeff_calorie_2)
        spent_calories = coeff_result * self.weight / self.M_IN_KM * time_in_minutes
        return spent_calories

class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 height: float,
                 ) -> None:
        super().__init__(action, duration, weight)
        self.height = height

    def get_spent_calories(self) -> float:
        coeff_calorie_3 = 0.035
        coeff_calorie_4 = 0.029
        time_in_minutes = self.duration * 60
        coeff_result1 = (coeff_calorie_3 * self.weight)
        coeff_result2 = (self.get_mean_speed()**2 // self.height) * coeff_calorie_4
        spent_calories = coeff_result1 + (coeff_result2 * self.weight) * time_in_minutes
        return spent_calories


class Swimming(Training):
    """Тренировка: плавание."""
    LEN_STEP = 1.35

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 length_pool: float,
                 count_pool: int,
                 ) -> None:
        super().__init__(action, duration, weight)
        self.length_pool = length_pool
        self.count_pool = count_pool

    def get_spent_calories(self) -> float:
        pass

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость при плавании в бассейне."""
        mean_speed = self.length_pool * self.count_pool / self.M_IN_KM / self.duration
        return mean_speed




def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    training_type_dict = {
        "SWM" : Swimming,
        "RUN" : Running,
        "WLK" : SportsWalking
    }
    pass
#   training_class_choice = training_type_dict[workout_type]
#   return 


def main(training: Training) -> None:
    """Главная функция."""
    pass


if __name__ == '__main__':
    packages = [
        ("SWM", [720, 1, 80, 25, 40]),
        ("RUN", [15000, 1, 75]),
        ("WLK", [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)

read_package("SWM", [720, 1, 80, 25, 40])