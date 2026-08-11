#include <stdio.h>
#include <math.h>
#ifdef _WIN32
#include <windows.h>
#endif

int main() {

    #ifdef _WIN32
        SetConsoleCP(65001);
        SetConsoleOutputCP(65001);
        #endif

    const double speed_light = 3e8; // скорость света
    const double k_e = 8.987e9; // константа для кулона
    const double g = 6.674e-11; // гравитационная постоянная
    const double g_e = 9.81; // ускорение свободного падения

    int choice = 0;

    while(choice !=11){
        printf("\n1.Формула Эпштейна\n");
        printf("2.Сила тока (Закон Ома)\n");
        printf("3.Закон Кулона\n");
        printf("4.Закон Всемирного тяготения\n");
        printf("5.Давление\n");
        printf("6.Плотность\n");
        printf("7.Сила тяжести\n");
        printf("8.Архимедова сила\n");
        printf("9.II закон Ньютона\n");
        printf("10.Ускорение\n");
        printf("11.Выход\n");
        printf("Ваш выбор: ");

        scanf("%d", &choice);

        switch (choice){
            case 1:
                printf("Формула Эпштейна E=mc²\n");
                double energy, mass;
                printf("Введите значение массы (в кг): ");
                scanf("%lf", &mass);
                energy = mass*pow(speed_light, 2);
                printf("\nОтвет: %.2e\n", energy);
                break;
            case 2:
                printf("Сила тока: I = U/R\n");
                double result_current, voltage, resistance;
                printf("\nВведите значение напряжения: ");
                scanf("%lf", &voltage);
                printf("\nВведите значение сопротивления: ");
                scanf("%lf", &resistance);
                if (resistance != 0){
                    result_current = voltage / resistance;
                    printf("\nОтвет: %.2e\n", result_current);
                }else{
                    printf("\nОшибка! Нельзя делить на ноль.\n");
                }
                break;
            case 3:
                printf("Закон Кулона");
                double f, q1, q2, r;
                printf("\nВведите количество первого заряда: ");
                scanf("%lf", &q1);
                printf("\nВведите количество второго заряда: ");
                scanf("%lf", &q2);
                printf("\nВведите расстояние между зарядами: ");
                scanf("%lf", &r);
                if (r != 0){
                    f = k_e * (fabs(q1*q2))/pow(r,2);
                    printf("\nОтвет: %.2e\n", f);
                }else{
                     printf("\nОшибка! Нельзя делить на ноль.\n");
                }
                break;
            case 4:
                printf("Закон Всемирного тяготения");
                double m1, m2;
                printf("\nВведите массу 1: ");
                scanf("%lf", &m1);
                printf("\nВведите массу 2: ");
                scanf("%lf", &m2);
                printf("\nВведите расстояние: ");
                scanf("%lf", &r);
                if (r != 0){
                    f = g * (m1 * m2)/pow(r, 2);
                    printf("\nОтвет: %.2e\n", f);
                }else{
                    printf("\nОшибка! Нельзя делить на ноль.\n");}
                break;
            case 5:
                printf("Давление");
                double s, p;
                printf("\nВведите площадь: ");
                scanf("%lf", &s);
                printf("\nВведите силу: ");
                scanf("%lf", &f);
                if (s != 0){
                    p = f/s;
                    printf("\nОтвет: %.2e\n", p);
                }else{
                    printf("\nОшибка! Нельзя делить на ноль.\n");
                }
                break;
            case 6:
                printf("Плотность");
                double rho, m, v;
                printf("\nВведите массу: ");
                scanf("%lf",&m);
                printf("\nВведите объем: ");
                scanf("%lf", &v);
                if (v != 0){
                    rho = m/v;
                    printf("\nОтвет: %.2e\n", rho);
                }else{
                    printf("\nОшибка! Нельзя делить на ноль.\n");
                }
                break;
            case 7:
                printf("Сила тяжести");
                printf("\nВведите значение массы: ");
                scanf("%lf", &m);
                f = m * g_e;
                printf("\nОтвет: %.2e\n", f);
                break;
            case 8:
                printf("Архимедова сила");
                double v_t;
                printf("\nВведите объем: ");
                scanf("%lf", &v_t);
                printf("\nВведите значение плотность: ");
                scanf("%lf", &rho);
                f = rho * g_e * v_t;
                printf("\nОтвет:%.2e \n", f);
                break;
            case 9:
                printf("II закон Ньютона");
                double a;
                printf("\nВведите значение массы: ");
                scanf("%lf", &m);
                printf("\nВведите значение ускорения: ");
                scanf("%lf", &a);
                f = m*a;
                printf("\nОтвет:%.2e \n",f);
                break;
            case 10:
                printf("Ускорение");
                double v0,t;
                printf("\nВведите значение скорости: ");
                scanf("%lf", &v);
                printf("\nВведите значение начальной скорости: ");
                scanf("%lf", &v0);
                printf("\nВведите значение времени: ");
                scanf("%lf", &t);
                if (t != 0){
                    a = (v-v0)/t;
                    printf("\nОтвет:%.2e\n", a);
                }else{
                    printf("\nОшибка! Нельзя делить на ноль.\n");
                }
                break;



        }
    }

    return 0;
}
