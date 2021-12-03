class InfoMessage:
    """Информационное сообщение о тренировке."""
    
    def __init__(self,
                 training_type: str,
                 duration: float,
                 distance: float,
                 speed: float,
                 calories: float,
                 ) -> None:
        self.training_type = training_type
        self.duration = duration
        self.distance = distance
        self.speed = speed
        self.calories = calories

    def сreate_message(self) -> str:
        return(f"Тип тренировки: {self.training_type}; Длительность: {self.duration} ч.;"
               f" Дистанция: {self.distance} км; Ср. скорость: {self.speed}"
               f" км/ч; Потрачено ккал: {self.calories}.")


class Training:
    """Базовый класс тренировки."""
    M_IN_KM: int = 1000
    LEN_STEP: float = 0.65
    training_type = ""
  
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
        #training_object = (self.training_type, self.duration, self.get_distance(), self.get_mean_speed(), self.get_spent_calories())
        info = InfoMessage(self.training_type, self.duration, self.get_distance(), self.get_mean_speed(), self.get_spent_calories())
        return info
        


class Running(Training):
    """Тренировка: бег."""
    training_type: str = "Тренировка по бегу"

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий при беге."""
        coeff_calorie_1 = 18
        coeff_calorie_2 = 20
        time_in_minutes = self.duration * 60
        coeff_result = (coeff_calorie_1 * self.get_mean_speed() - coeff_calorie_2)
        spent_calories = coeff_result * self.weight / self.M_IN_KM * time_in_minutes
        return spent_calories


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    training_type: str = "Тренировка по спортивной хотьбе"

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 height: float,
                 ) -> None:
        super().__init__(action, duration, weight)
        self.height = height

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий при хотьбе."""
        coeff_calorie_3 = 0.035
        coeff_calorie_4 = 0.029
        time_in_minutes = self.duration * 60
        coeff_result_1 = (coeff_calorie_3 * self.weight)
        coeff_result_2 = (self.get_mean_speed()**2 // self.height) * coeff_calorie_4
        spent_calories = coeff_result_1 + (coeff_result_2 * self.weight) * time_in_minutes
        return spent_calories


class Swimming(Training):
    """Тренировка: плавание."""
    LEN_STEP: float = 1.35
    training_type: str = "Тренировка по плаванию"

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
        """Получить количество затраченных калорий при плавании."""
        coeff_calorie_5 = 1.1
        coeff_calorie_6 = 2
        coeff_result_3 = (self.get_mean_speed() + coeff_calorie_5)
        spent_calories =  coeff_result_3 * coeff_calorie_6 * self.weight
        return spent_calories

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость при плавании в бассейне."""
        all_dist_pool = self.length_pool * self.count_pool
        mean_speed = all_dist_pool / self.M_IN_KM / self.duration
        return mean_speed


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    training_type_dict = {
        "SWM" : Swimming,
        "RUN" : Running,
        "WLK" : SportsWalking
    }
    training = training_type_dict[workout_type](*data)
    return training


def main(training: Training) -> str:
    """Главная функция."""
    info = training.show_training_info()
    print(info.сreate_message())


if __name__ == '__main__':
    packages = [
        ("SWM", [720, 1, 80, 25, 40]),
        ("RUN", [15000, 1, 75]),
        ("WLK", [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)

