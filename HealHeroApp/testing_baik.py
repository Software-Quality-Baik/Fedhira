import time  # Impor modul time untuk penundaan
import unittest  # Impor modul unittest untuk pengujian
from selenium import webdriver  # Impor modul webdriver dari Selenium untuk otomatisasi browser
from selenium.webdriver.common.by import By  # Impor modul By dari Selenium untuk memilih elemen
from selenium.webdriver.common.keys import Keys  # Impor modul Keys dari Selenium untuk mengirim kunci


class SystemTest(unittest.TestCase):
    def setUp(self):
        # Inisialisasi WebDriver
        self.driver = webdriver.Chrome()

    def tearDown(self):
        # Tambahkan penundaan waktu sebelum menutup WebDriver
        time.sleep(5)

        # Menutup WebDriver
        self.driver.quit()

    def login(self, username, password):
        # Membuka halaman login
        self.driver.get("https://healhero.my.id/signin.html")

        # Mencari elemen input username dan password menggunakan XPath
        email_input = self.driver.find_element(By.XPATH, "//input[@id='email']")
        password_input = self.driver.find_element(By.XPATH, "//input[@id='password']")

        # Memasukkan nama pengguna dan kata sandi
        email_input.send_keys(username)
        password_input.send_keys(password)

        time.sleep(2)

        # Klik tombol Login
        button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        button.click()

        time.sleep(2)

        # Cari dan klik tombol OK pada popup
        swal = self.driver.find_element(By.CLASS_NAME, "swal2-confirm")
        swal.click()

    def cek_home(self):
        # Membuka halaman cek kesehatan
        self.driver.get("https://healhero.my.id/pengguna/index.html")

        time.sleep(2)

        # Lakukan pengujian cek kesehatan
        # Lakukan implementasi pengujian cek kesehatan di sini

    def cek_kesehatan(self):
        # Membuka halaman cek kesehatan
        self.driver.get("https://healhero.my.id/pengguna/cekkesehatan.html")

        time.sleep(2)

        # Lakukan pengujian cek kesehatan
        # Lakukan implementasi pengujian cek kesehatan di sini

    def cek_kebugaran(self):
        # Membuka halaman cek kebugaran
        self.driver.get("https://healhero.my.id/pengguna/cekkebugaran.html")

        time.sleep(2)

        # Mencari elemen input menggunakan ID
        age_input = self.driver.find_element(By.ID, "age")
        gender_input = self.driver.find_element(By.ID, "gender")
        exerciseTime_input = self.driver.find_element(By.ID, "exerciseTime")
        exerciseDays_input = self.driver.find_element(By.ID, "exerciseDays")
        smoking_input = self.driver.find_element(By.ID, "smoking")

        # Memasukkan nilai ke dalam input
        age_input.send_keys("20")
        gender_input.send_keys(Keys.ARROW_DOWN)
        exerciseTime_input.send_keys("10")
        exerciseDays_input.send_keys("3")
        smoking_input.send_keys(Keys.ARROW_DOWN)

        # Tunggu hingga tombol submit muncul
        time.sleep(2)

        # Klik tombol Submit
        button = self.driver.find_element(By.XPATH, '//button[@type="button"]')
        button.click()

    def test_system_flow(self):
        # Jalankan pengujian login
        self.login("putri1@gmail.com", "putricantik")

        self.cek_home()

        # Jalankan pengujian cek kesehatan
        self.cek_kesehatan()

        # Jalankan pengujian cek kebugaran
        self.cek_kebugaran()


if __name__ == "__main__":
    unittest.main()