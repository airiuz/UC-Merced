## Tensorflow datasets: uc_merced dataseti

#### 1. ```uc_merced``` dataseti haqida qisqacha ma'lumot

UC-merced - har bir classi 100 ta tasvirdan iborat bo'lgan 21 ta sinfli quruqlikdagi masofadan zondlash tasvir ma'lumotlari to'plami hisoblanadi. Rasmlar USGS National Map Urban Area Imagery to'plamidan olingan va mamlakatlarning turli shaharlari ustidan qo'lda olingan. Ko'pgina tasvirlar 256x256 piksel bo'lsada, har xil shaklga ega 44 ta rasm mavjud. Dataset parametrlari:

* Versiya: 2.0.0 
* Manba: https://www.tensorflow.org/datasets/catalog/uc_merced
* Manba kodi: tfds.image_classification.UcMerced
* Dataset hajmi: 317.07 MB 

<p align="center">
  <img src="https://github.com/MisterFoziljon/UC-Merced/blob/main/uc_merced-2.0.0.png" />
</p>

#### 2. Loyihani yuklab olish uchun quyidagi ketma-ketlikni bajaring:
  * `windows+R` klavishlarini bosing va paydo bo'lgan oynaga `cmd` buyrug'ini yozing OK tugmachasini bosing.
  
  ![cmd](https://github.com/MisterFoziljon/Fashion-MNIST/blob/main/rasmlar/cmd.png)

  * Loyihani quyidagi link yordamida yuklab oling. (Loyiha uchun yaratilgan fayl adresni o'zingiz ko'rsatishingiz mumkin)

        C:\> git clone https://github.com/MisterFoziljon/UC-Merced.git

  * Loyiha joylashgan faylga kiring.
         
        C:\> cd UC-Merced


#### 3. Proyektni ishlatish uchun kerakli modullarni virtual environment yaratib o'rnatib oling.
* O'zingizdagi pip ni so'nggi versiyasiga yangilang.

        C:\UC-Merced> python -m pip install --upgrade pip
        
* virtual environment yaratish uchun virtualenv modulini o'rnating.
        
        C:\UC-Merced> python -m pip install --user virtualenv

* Yangi environment yaratish uchun unga nom bering.
        
        C:\UC-Merced> python -m venv sizning_env
        
* Virtual environmentni ishga tushiring(aktivlashtiring).
        
        C:\UC-Merced> sizning_env\Scripts\activate.bat
        
* Virtual environment ichiga loyiha ishlashi uchun kerakli bo'lgan modullarni o'rnating (requirements.txt faylining ichida barchasi mavjud).
        
        (sizning_env) C:\UC-Merced> pip install -r requirements.txt


#### 4. Proyektni ishlatish uchun jupyter notebook ni ishga tushiring.

        (sizning_env) C:\UC-Merced> jupyter notebook
        
  * ```UC_Merged.ipynb``` ni ishga tushiring. 
  * Usbu notebookda [Tensorflow.org](https://www.tensorflow.org/) saytidagi [uc_merced](https://www.tensorflow.org/datasets/catalog/uc_merced?hl=ru) datasetini o'qib olish, uni train va test datalariga ajratish, datalarni size va shape larini train uchun moslash hamda normallashtirish ko'rsatilgan.
  
  * Dataset yordamida 2 xil usulda Convolutional Neural Network ishlab chiqilgan va u yordamida model train va evaluate qilingan.
    - VGG-19 arxitekturasi transfer learning qilingan ([model](https://drive.google.com/drive/folders/1FiLKxkGaaegD26nwx1fhCYZjRfY7Oj7D?usp=share_link)).
    - VGG-19 arxitekturasi noldan qurilgan ([model](https://drive.google.com/file/d/1GvXvsGEg_qmEngBVGrkYQ6TiGVtR3m0b/view?usp=share_linkd)).
   
   | **Arxitektura ko'rinishi** | **Validation Loss** | **Validation Accuracy** | **Parametrlar soni** |
   |---------------|-----------------|---------------|-----------------|
   | **VGG-19 transfer learning** |0.4658|0.89| 74 180 693 |
   | **VGG-19 arxitektura** |3.04909|0.3|74 166 357|
  * Tensorboardga har bir epochdagi loss va accuracy qiymatlari saqlab borilgan. ([Tensorboard](https://tensorboard.dev/experiment/jgldeOnBQFKW0s6voTOrfQ/#scalars))
<p align="center">
  <img src="https://github.com/MisterFoziljon/UC-Merced/blob/main/tensorboard.png" />
</p>

#### 5. Proyektni streamlit yordamida deploy qilish.

        (sizning_env) C:\UC-Merced> streamlit run streamlit.py

  * Proyekt ```local server```da ishga tushadi va quyidagicha ko'rinishda bo'ladi:


![streamlit1](https://github.com/MisterFoziljon/UC-Merced/blob/main/streamlit1.png)
  
  * Rasm faylini yuklab oling va ```Predict``` tugmachasini bosing. Model yuklab olingan tasvirni qaysi turkumga tegishli ekanligini bashorat qiladi. Bundan tashqari softmaxdan chiqqan ehtimollik natijasi ham ekranga chiqadi.


![streamlit3](https://github.com/MisterFoziljon/UC-Merced/blob/main/streamlit2.png)
