import os
import json
import random

from scryptlib import (
        compile_contract, build_contract_class, build_type_classes
        )

contract = './res/testKeccak256.scrypt' 

compiler_result = compile_contract(contract, debug=False)
#desc = compiler_result.to_desc()
#
## Load desc instead:
##with open('./out/testKeccak256_desc.json', 'r') as f:
##    desc = json.load(f)
#
#type_classes = build_type_classes(desc)
#
#TestKeccak256 = build_contract_class(desc)
#test_keccak256 = TestKeccak256()


