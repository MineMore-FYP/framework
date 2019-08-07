from __future__ import print_function
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import sys, os

import pprint
import tempfile

import tensorflow as tf
import tensorflow_transform as tft
import tensorflow_transform.beam.impl as tft_beam
from tensorflow_transform.tf_metadata import dataset_metadata
from tensorflow_transform.tf_metadata import dataset_schema

raw_data = [
      {'x': 1, 'y': 1, 's': 'hello'},
      {'x': 2, 'y': 2, 's': 'world'},
      {'x': 3, 'y': 3, 's': 'hello'}
  ]

raw_data_metadata = dataset_metadata.DatasetMetadata(
    dataset_schema.from_feature_spec({
        'y': tf.FixedLenFeature([], tf.float32),
        'x': tf.FixedLenFeature([], tf.float32),
        's': tf.FixedLenFeature([], tf.string),
    }))


def preprocessing_fn(inputs):
    """Preprocess input columns into transformed columns."""
    x = inputs['x']
    y = inputs['y']
    s = inputs['s']
    x_centered = x - tft.mean(x)
    y_normalized = tft.scale_to_0_1(y)
    s_integerized = tft.compute_and_apply_vocabulary(s)
    x_centered_times_y_normalized = (x_centered * y_normalized)
    return {
        'x_centered': x_centered,
        'y_normalized': y_normalized,
        's_integerized': s_integerized,
        'x_centered_times_y_normalized': x_centered_times_y_normalized,
    }

def main():
  # Ignore the warnings
  with tft_beam.Context(temp_dir=tempfile.mkdtemp()):
    transformed_dataset, transform_fn = (  # pylint: disable=unused-variable
        (raw_data, raw_data_metadata) | tft_beam.AnalyzeAndTransformDataset(
            preprocessing_fn))

  transformed_data, transformed_metadata = transformed_dataset  # pylint: disable=unused-variable

  print('\nRaw data:\n{}\n'.format(pprint.pformat(raw_data)))
  print('Transformed data:\n{}'.format(pprint.pformat(transformed_data)))

if __name__ == '__main__':
  main()
