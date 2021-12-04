class InfoMessage:
    """Информационное сообщение о тренировке."""

    def __init__(
            self,
            training_type: str,
            duration: float,
            distance: float,
            speed: float,
            calories: float) -> None:
        self.training_type = training_type
        self.duration = duration
        self.distance = distance
        self.speed = speed
        self.calories = calories

    def get_message(self) -> str:
        return (f"Тип тренировки: {self.training_type}; "
                f"Длительность: {self.duration:.3f} ч.; "
                f"Дистанция: {self.distance:.3f} км; "
                f"Ср. скорость: {self.speed:.3f} км/ч; "
                f"Потрачено ккал: {self.calories:.3f}.")


class Training:
    """Базовый класс тренировки."""

    M_IN_KM: int = 1000
    LEN_STEP: float = 0.65
    TRAINIG_TYPE = ""

    def __init__(
            self,
            action: int,
            duration: float,
            weight: float) -> None:
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
        info = InfoMessage(
            self.TRAINIG_TYPE,
            self.duration,
            self.get_distance(),
            self.get_mean_speed(),
            self.get_spent_calories(),
        )
        return info


class Running(Training):
    """Тренировка: бег."""

    TRAINIG_TYPE = "Running"

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий при беге."""
        coeff_cal_1 = 18
        coeff_cal_2 = 20
        time_in_minutes = self.duration * 60
        intermed_res = coeff_cal_1 * self.get_mean_speed() - coeff_cal_2
        spent_cal = intermed_res * self.weight / self.M_IN_KM * time_in_minutes
        return spent_cal


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""

    TRAINIG_TYPE = "SportsWalking"

    def __init__(
            self,
            action: int,
            duration: float,
            weight: float,
            height: float) -> None:
        super().__init__(action, duration, weight)
        self.height = height

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий при хотьбе."""
        coeff_cal_3 = 0.035
        coeff_cal_4 = 0.029
        time_in_minutes = self.duration * 60
        intermediate_res_1 = coeff_cal_3 * self.weight
        intermediate_res_2 = self.get_mean_speed()**2 // self.height
        intermediate_res_3 = intermediate_res_2 * coeff_cal_4 * self.weight
        spent_cal = (intermediate_res_1 + intermediate_res_3) * time_in_minutes
        return spent_cal


class Swimming(Training):
    """Тренировка: плавание."""

    LEN_STEP: float = 1.38
    TRAINIG_TYPE = "Swimming"

    def __init__(
            self,
            action: int,
            duration: float,
            weight: float,
            length_pool: float,
            count_pool: int) -> None:
        super().__init__(action, duration, weight)
        self.length_pool = length_pool
        self.count_pool = count_pool

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий при плавании."""
        coeff_calorie_5 = 1.1
        coeff_calorie_6 = 2
        intermediate_res_4 = self.get_mean_speed() + coeff_calorie_5
        spent_calories = intermediate_res_4 * coeff_calorie_6 * self.weight
        return spent_calories

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость при плавании в бассейне."""
        all_dist_pool = self.length_pool * self.count_pool
        mean_speed = all_dist_pool / self.M_IN_KM / self.duration
        return mean_speed


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""

    train_dict: dict = {
        "SWM": Swimming,
        "RUN": Running,
        "WLK": SportsWalking,
    }
    training: Training = train_dict[workout_type](*data)
    return training


def main(training: Training) -> None:
    """Главная функция."""
    info = training.show_training_info()
    print(info.get_message())


if __name__ == "__main__":
    packages = [
        ("SWM", [720, 1, 80, 25, 40]),
        ("RUN", [15000, 1, 75]),
        ("WLK", [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
