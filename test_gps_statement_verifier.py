import os
import json
import random

from scryptlib import (
        compile_contract, build_contract_class, build_type_classes
        )

contract = './res/testGPSStatementVerifier.scrypt' 

compiler_result = compile_contract(contract, debug=True)
desc = compiler_result.to_desc()

# Load desc instead:
#with open('./out/testGPSStatementVerifier_desc.json', 'r') as f:
#    desc = json.load(f)

type_classes = build_type_classes(desc)

