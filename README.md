# 🎓 On the Reliability of Backdoor Accuracy as a Metric

This repository documents the **implementation and experimental results** for the thesis, "On the Reliability of Backdoor Accuracy as a Metric."

-----

## 📄 Thesis Report

[The complete thesis document](./Thesis_Report_Nishant_Ingle.pdf) is compiled report in PDF format.

Known Issue: The table rows/column lines seem to disappear when a page from the report is zoomed out in *Adobe Acrobat reader*. This issue is related to how the document is rendered and is not present when the PDF is opened using Chrome.

-----

## 🎯 Scope

This research systematically investigates the reliability of **Backdoor Accuracy** as a performance metric within the context of **backdoored machine learning models**. The study focuses specifically on backdoors induced by two distinct trigger types: **pixel-based triggers** and **noise-based triggers** .

For **pixel-based triggers**, we conduct a comprehensive analysis of the influence of several critical factors:

  * Trigger **intensity**.
  * Trigger **color**.
  * Trigger **location**.
  * Trigger **kernel shape**.

For **noise-based triggers**, the investigation focuses on:

  * Noise **intensity**.
  * Noise **location**.

The primary performance metrics under evaluation is the **Backdoor Accuracy** (BA) on fully poisoned datasets.

-----

## 💻 Datasets and Experimental Code Structure

All source code and experimental notebooks are organized within the [`Code`](./Code) directory.

### Datasets 💾

The image classification datasets can be found within the [`Datasets`](./Datasets) subdirectory.
Although, we have used the datasets from torchvision.datasets library:

  * **CIFAR-10**
  * **MNIST**

The pre-trained poisoned models can be found on my [Kaggle profile](https://www.kaggle.com/inglenishant/datasets)
wrapped in Kaggle datasets. That said, training the models from scratch is highly recommended.

-----
