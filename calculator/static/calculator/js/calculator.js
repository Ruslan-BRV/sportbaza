document.querySelector('button[value="Рассчитать"]').addEventListener('click', calculateCalories);

function calculateCalories() {
    weight = Number(document.getElementById('weight').value);
    height = Number(document.getElementById('height').value);
    age = Number(document.getElementById('age').value);
    gender = document.querySelector('input[name="gender"]:checked').value;
    activityLevel = document.getElementById('activity').value;
    // Константы для расчета BMR (базового метаболического уровня)
    const BMR_MEN = 66 + (13.7  *  weight) + (5  *  height) - (6.8  *  age);
    const BMR_WOMEN = 655 + (9.6  *  weight) + (1.8  *  height) - (4.7  *  age);

    // Константы для расчета коэффициента активности
    const ACTIVITY_LEVEL = {
        sedentary: 1.2,
        lightlyActive: 1.375,
        moderatelyActive: 1.55,
        veryActive: 1.725,
        extraActive: 1.9
    };

    // Проверка пола
    let bmr;
    if (gender === 'male') {
        bmr = BMR_MEN;
    } else if (gender === 'female') {
        bmr = BMR_WOMEN;
    } else {
        console.error('Неверный пол. Пожалуйста, введите "male" или "female".');
        return;
    }

    // Проверка уровня активности
    let activityLevelMultiplier = ACTIVITY_LEVEL[activityLevel];
    if (!activityLevelMultiplier) {
        console.error('Неверный уровень активности. Пожалуйста, введите "sedentary", "lightlyActive", "moderatelyActive", "veryActive" или "extraActive".');
        return;
    }

    // Расчет общего количества калорий
    let totalCalories = bmr  *  activityLevelMultiplier;
    let calories = document.getElementById('calories')
    calories.innerText = `Ваше общее количество калорий в сутки: ${totalCalories.toFixed(2)} ккал`
}

