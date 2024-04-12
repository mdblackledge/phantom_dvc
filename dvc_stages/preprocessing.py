""" Runs all preprocessing steps """

import sys
import os

import numpy as np
import SimpleITK as sitk  # noqa


def run_stage(raw_data_path: str, out_path: str) -> None:
    os.makedirs(out_path, exist_ok=True)
    mask_image = sitk.ReadImage(os.path.join(raw_data_path, 'mask.nrrd'))
    phantom_image = sitk.ReadImage(os.path.join(raw_data_path, 'phantom.nrrd'))
    mask_array = sitk.GetArrayFromImage(mask_image)
    phantom_array = sitk.GetArrayFromImage(phantom_image)
    np.save(os.path.join(out_path, "mask.npy"), mask_array)
    np.save(os.path.join(out_path, "phantom.npy"), phantom_array)


if __name__ == "__main__":
    run_stage(sys.argv[1], sys.argv[2])
