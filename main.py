import asyncio
from apiService import create_app
import multiprocessing


def run_flask_app(shared_variable,startBot):
    flask_app = create_app(shared_variable,startBot)
    flask_app.run(host='0.0.0.0', port=4000)

    print("flask")

async def main():
    with multiprocessing.Manager() as manager:
        smsCode = manager.Value('sms', 0)
        data = manager.Value('data', [{ "city": "Gaziantep",
            "office": "Gaziantep Ofis",
            "getapplicationtype": "Ticari",
            "officetype": "STANDART",
            "name": "Ömer",
            "surname": "Erbalta",
            "birthday": "03",
            "birthmonth": "10",
            "birthyear": "2000",
            "passport": "43453553135",
            "phone": "5394230669",
            "email": "erbaltadeveloper@gmail.com"},
            [{ "city": "Gaziantep",
            "office": "Gaziantep Ofis",
            "getapplicationtype": "Ticari",
            "officetype": "STANDART",
            "name": "Ömer",
            "surname": "Erbalta",
            "birthday": "03",
            "birthmonth": "10",
            "birthyear": "2000",
            "passport": "43453553135",
            "phone": "5394230669",
            "email": "erbaltadeveloper@gmail.com"},
            { "city": "Eskişehir",
            "office": "Gaziantep Ofis",
            "getapplicationtype": "Ticari",
            "officetype": "STANDART",
            "name": "Ömer",
            "surname": "Erbalta",
            "birthday": "03",
            "birthmonth": "10",
            "birthyear": "2000",
            "passport": "43453553135",
            "phone": "5394230669",
            "email": "erbaltadeveloper@gmail.com"}],

             { "city": "Eskişehir",
            "office": "Gaziantep Ofis",
            "getapplicationtype": "Ticari",
            "officetype": "STANDART",
            "name": "Ömer",
            "surname": "Erbalta",
            "birthday": "03",
            "birthmonth": "10",
            "birthyear": "2000",
            "passport": "43453553135",
            "phone": "5394230669",
            "email": "erbaltadeveloper@gmail.com"}])

        api_process = multiprocessing.Process(target=run_flask_app, args=(smsCode,data))
        api_process.start()

      #  await data_fill_main(smsCode,data)

if __name__ == '__main__':

    asyncio.run(main())
