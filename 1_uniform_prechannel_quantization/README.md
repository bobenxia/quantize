## 1_uniform_perchannel_quantization

### 文件说明

- `ckpt`存放模型

- `a_basic_quant.ipynb` 包含了量化公式计算、自定义量化层

- `b_model.ipynb`定义了网络

- `c_train_and_test.ipynb`用于训练全精度模型

- `d_psot_training_quantize.ipynb`用于量化模型

- `help_to_know_quantization.ipynb`教学理解用途，帮助理解相关流程

- `Ipynb_importer.py`用于解析ipynb文件，从而实现不同ipynb文件之间的调用

- `hash_to_test.ipynb`虽然可以通过 Ipynb_import.py文件实现在不同 ipynb文件中互相调用模块，但是在某一 ipynb 调试中跳转到另一个 ipynb 中的模块的时候，无法给出在其他 ipynb文件中明确位置。

  因此，将所有要使用的模块合并到这个文件中，方便调试修改。

- `*_test.ipynb`测试用的文件，无用，未删，留着以后可能会用到

