from dataclasses import dataclass
from typing import ClassVar


@dataclass
class InfoMessage:
    """Информационное сообщение о тренировке."""
    training_type: str
    duration: float
    distance: float
    speed: float
    calories: float

    def get_message(self) -> str:
        return (f"Тип тренировки: {self.training_type}; "
                f"Длительность: {self.duration:.3f} ч.; "
                f"Дистанция: {self.distance:.3f} км; "
                f"Ср. скорость: {self.speed:.3f} км/ч; "
                f"Потрачено ккал: {self.calories:.3f}.")


@dataclass
class Training:
    """Базовый класс тренировки."""
    action: int
    duration: float
    weight: float
    LEN_STEP: ClassVar[float] = 0.65
    M_IN_KM: ClassVar[int] = 1000
    HOUR_IN_MIN: ClassVar[int] = 60
    COEFF_RUN: ClassVar[int] = 18
    COEFF_RUN_2: ClassVar[int] = 20
    COEFF_WALK: ClassVar[float] = 0.035
    COEFF_WALK_2: ClassVar[float] = 0.029
    COEFF_SWIMING: ClassVar[float] = 1.1
    COEFF_SWIMING_2: ClassVar[int] = 2

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        return self.action * self.LEN_STEP / self.M_IN_KM

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        full_distance = self.get_distance()
        return full_distance / self.duration

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        raise NotImplementedError(
            "В Методе сабкласса должна быть прописана реализация"
        )

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        return InfoMessage(
            type(self).__name__,
            self.duration,
            self.get_distance(),
            self.get_mean_speed(),
            self.get_spent_calories(),
        )


@dataclass
class Running(Training):
    """Тренировка: бег."""

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий при беге."""
        time_in_min = self.duration * self.HOUR_IN_MIN
        mean_speed = self.get_mean_speed()
        part_of_formula = self.COEFF_RUN * mean_speed - self.COEFF_RUN_2
        return part_of_formula * self.weight / self.M_IN_KM * time_in_min


@dataclass
class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    height: float

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий при хотьбе."""
        time_in_minutes = self.duration * self.HOUR_IN_MIN
        part_of_formula = self.COEFF_WALK * self.weight
        part_of_formula_2 = self.get_mean_speed()**2 // self.height
        part_of_formula_3 = part_of_formula_2 * self.COEFF_WALK_2 * self.weight
        return (part_of_formula + part_of_formula_3) * time_in_minutes


@dataclass
class Swimming(Training):
    """Тренировка: плавание."""
    length_pool: float = 1
    count_pool: int = 1
    LEN_STEP: ClassVar[float] = 1.38

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий при плавании."""
        part_of_formula = self.get_mean_speed() + self.COEFF_SWIMING
        return part_of_formula * self.COEFF_SWIMING_2 * self.weight

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость при плавании в бассейне."""
        all_dist_pool = self.length_pool * self.count_pool
        return all_dist_pool / self.M_IN_KM / self.duration


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    train_dict: dict = {
        "SWM": Swimming,
        "RUN": Running,
        "WLK": SportsWalking,
    }
    if workout_type not in train_dict:
        # На самом деле не до конца понял этот модуль
        # Да, сейчас выкидываю сообщение c типом, но все равно код падает.
        # Нужно ли делать что-то еще?
        raise KeyError(
            "вызывающая сторона передала workout_type, "
            "которого в нашем словаре нет - " + workout_type
            + ". Проверьте данные на ввод, пожалуйста"
        )
    else:
        return train_dict[workout_type](*data)


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
