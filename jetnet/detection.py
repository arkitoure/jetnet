# SPDX-FileCopyrightText: Copyright (c) <year> NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from abc import abstractmethod

from jetnet.polygon import Polygon
from jetnet.classification import Classification
from jetnet.model import Model
from jetnet.image import Image
from jetnet.binary_mask import BinaryMask
from pydantic import BaseModel
from dataclasses import dataclass

from typing import Optional, Sequence


class Detection(BaseModel):

    class Config:
        arbitrary_types_allowed = True

    boundary: Polygon
    classification: Optional[Classification] = None
    mask: Optional[BinaryMask] = None


class DetectionSet(BaseModel):

    class Config:
        arbitrary_types_allowed = True

    detections: Sequence[Detection]


class DetectionModel(Model[Image, DetectionSet]):
    
    @abstractmethod
    def get_labels(self) -> Sequence[str]:
        raise NotImplementedError
