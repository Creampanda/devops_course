# Инструкция по установке и подключению Jenkins

## Подключение к ВМ с пробросом порта

Необходимо пробросить порт на сервер, т.к. Jenkins имеет UI

```bash
ssh <user>@<address> -p <port> -L 8080:127.0.0.1:8080
```

## Установка на ВМ

1. Установим java

```bash
sudo apt install -y openjdk-17-jre-headless
```

2. Запустим установку следующими командами

```bash
sudo wget -O /usr/share/keyrings/jenkins-keyring.asc \
  https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key
echo "deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc]" \
  https://pkg.jenkins.io/debian-stable binary/ | sudo tee \
  /etc/apt/sources.list.d/jenkins.list > /dev/null
sudo apt-get update
sudo apt-get install jenkins
```

3. Ставим инструмент для сборки docker образов

```bash
apt install buildah
```

4.

```bash
echo jenkins:10000:65536 >> /etc/subuid
echo jenkins:10000:65536 >> /etc/subgid
```

<details><summary>Объяснение команд</summary>
UID (User ID) — это уникальный номер, который присваивается каждому пользователю. GID (Group ID) — это номер, который присваивается каждой группе пользователей.

subuid и subgid — это системы, которые позволяют администраторам задавать "дополнительные" идентификаторы для пользователей и групп. Это нужно для того, чтобы один пользователь мог действовать от имени нескольких пользователей внутри системы. Эти дополнительные идентификаторы используются в основном при работе с контейнерами, такими как Docker.

Когда Jenkins запускает контейнеры (например, для выполнения задач по сборке и тестированию в изолированной среде), он может использовать любой UID и GID из указанного диапазона (10000-75535) внутри этих контейнеров. Это означает, что если процесс внутри контейнера будет скомпрометирован, он не сможет взаимодействовать с основной системой так, как если бы он запущен был под реальным UID/GID Jenkins на хосте.

</details>

## Запуск Jenkins

После успешно выполненных шагов, будет доступен Jenkins UI по адресу http://localhost:8080/
![alt text](images/image.png)

```bash
cat /var/lib/jenkins/secrets/initialAdminPassword
```

Устанавливаем предложенные плагины и после выполнения всех шагов, попадаем на главную страницу.
![alt text](images/image-1.png)

## Gitlab + Jenkins

1. Необходимо создать Access token для репозитория
   ![alt text](images/image-2.png)
   ![alt text](images/image-3.png)
2. Необходимо добавить токен в Jenkins. Переходим в Dashboard-> Manage Jenkins-> Credentials-> System и добавляем токен
   ![alt text](images/image-4.png)

## Первая задача в Jenkins

1. Создадим новую задачу
   ![alt text](images/image-6.png)
2. Добавим параметры PORT и BRANCH_NAME
   ![alt text](images/image-10.png)
3. Настроим Branch Specifier
   ![alt text](images/image-11.png)
4. Добавим scheduler
   ![alt text](images/image-12.png)
5. Добавим build step
   ![alt text](images/image-13.png)
6. Запустим сборку
   ![alt text](images/image-14.png)
   ![alt text](images/image-16.png)
   ![alt text](images/image-15.png)
