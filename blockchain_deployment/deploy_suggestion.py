import json

from solcx import compile_standard, install_solc
from web3 import Web3


class Deploy_Suggestion:
    def __init__(self, private_key, address):
        """

        @note : initializes the abi . w3
        :param private_key: string
        :param address: string - user user_address
        """
        with open("/home/nilay/PROJECTS/HACK/Hestia/blockchain_deployment/Suggestion.sol", "r") as file:
            self.suggestion_file = file.read()
        self.user_address = address
        self.pvt_key = private_key
        # for connecting to ganache
        self.w3 = Web3(Web3.HTTPProvider("http://0.0.0.0:8545"))
        self.chain_id = 1337

        # Getting the latest transaction
        self.nonce = self.w3.eth.getTransactionCount(self.user_address)
        self.count = 0

        # To check if the user has voted or not
        self.flag = False
        # get bytecode
        self.bytecode =  {"generatedSources": [
              {
                "ast": {
                  "nodeType": "YulBlock",
                  "src": "0:1321:1",
                  "statements": [
                    {
                      "body": {
                        "nodeType": "YulBlock",
                        "src": "70:80:1",
                        "statements": [
                          {
                            "nodeType": "YulAssignment",
                            "src": "80:22:1",
                            "value": {
                              "arguments": [
                                {
                                  "name": "offset",
                                  "nodeType": "YulIdentifier",
                                  "src": "95:6:1"
                                }
                              ],
                              "functionName": {
                                "name": "mload",
                                "nodeType": "YulIdentifier",
                                "src": "89:5:1"
                              },
                              "nodeType": "YulFunctionCall",
                              "src": "89:13:1"
                            },
                            "variableNames": [
                              {
                                "name": "value",
                                "nodeType": "YulIdentifier",
                                "src": "80:5:1"
                              }
                            ]
                          },
                          {
                            "expression": {
                              "arguments": [
                                {
                                  "name": "value",
                                  "nodeType": "YulIdentifier",
                                  "src": "138:5:1"
                                }
                              ],
                              "functionName": {
                                "name": "validator_revert_t_address",
                                "nodeType": "YulIdentifier",
                                "src": "111:26:1"
                              },
                              "nodeType": "YulFunctionCall",
                              "src": "111:33:1"
                            },
                            "nodeType": "YulExpressionStatement",
                            "src": "111:33:1"
                          }
                        ]
                      },
                      "name": "abi_decode_t_address_fromMemory",
                      "nodeType": "YulFunctionDefinition",
                      "parameters": [
                        {
                          "name": "offset",
                          "nodeType": "YulTypedName",
                          "src": "48:6:1",
                          "type": ""
                        },
                        {
                          "name": "end",
                          "nodeType": "YulTypedName",
                          "src": "56:3:1",
                          "type": ""
                        }
                      ],
                      "returnVariables": [
                        {
                          "name": "value",
                          "nodeType": "YulTypedName",
                          "src": "64:5:1",
                          "type": ""
                        }
                      ],
                      "src": "7:143:1"
                    },
                    {
                      "body": {
                        "nodeType": "YulBlock",
                        "src": "219:80:1",
                        "statements": [
                          {
                            "nodeType": "YulAssignment",
                            "src": "229:22:1",
                            "value": {
                              "arguments": [
                                {
                                  "name": "offset",
                                  "nodeType": "YulIdentifier",
                                  "src": "244:6:1"
                                }
                              ],
                              "functionName": {
                                "name": "mload",
                                "nodeType": "YulIdentifier",
                                "src": "238:5:1"
                              },
                              "nodeType": "YulFunctionCall",
                              "src": "238:13:1"
                            },
                            "variableNames": [
                              {
                                "name": "value",
                                "nodeType": "YulIdentifier",
                                "src": "229:5:1"
                              }
                            ]
                          },
                          {
                            "expression": {
                              "arguments": [
                                {
                                  "name": "value",
                                  "nodeType": "YulIdentifier",
                                  "src": "287:5:1"
                                }
                              ],
                              "functionName": {
                                "name": "validator_revert_t_uint256",
                                "nodeType": "YulIdentifier",
                                "src": "260:26:1"
                              },
                              "nodeType": "YulFunctionCall",
                              "src": "260:33:1"
                            },
                            "nodeType": "YulExpressionStatement",
                            "src": "260:33:1"
                          }
                        ]
                      },
                      "name": "abi_decode_t_uint256_fromMemory",
                      "nodeType": "YulFunctionDefinition",
                      "parameters": [
                        {
                          "name": "offset",
                          "nodeType": "YulTypedName",
                          "src": "197:6:1",
                          "type": ""
                        },
                        {
                          "name": "end",
                          "nodeType": "YulTypedName",
                          "src": "205:3:1",
                          "type": ""
                        }
                      ],
                      "returnVariables": [
                        {
                          "name": "value",
                          "nodeType": "YulTypedName",
                          "src": "213:5:1",
                          "type": ""
                        }
                      ],
                      "src": "156:143:1"
                    },
                    {
                      "body": {
                        "nodeType": "YulBlock",
                        "src": "399:346:1",
                        "statements": [
                          {
                            "body": {
                              "nodeType": "YulBlock",
                              "src": "445:16:1",
                              "statements": [
                                {
                                  "expression": {
                                    "arguments": [
                                      {
                                        "kind": "number",
                                        "nodeType": "YulLiteral",
                                        "src": "454:1:1",
                                        "type": "",
                                        "value": "0"
                                      },
                                      {
                                        "kind": "number",
                                        "nodeType": "YulLiteral",
                                        "src": "457:1:1",
                                        "type": "",
                                        "value": "0"
                                      }
                                    ],
                                    "functionName": {
                                      "name": "revert",
                                      "nodeType": "YulIdentifier",
                                      "src": "447:6:1"
                                    },
                                    "nodeType": "YulFunctionCall",
                                    "src": "447:12:1"
                                  },
                                  "nodeType": "YulExpressionStatement",
                                  "src": "447:12:1"
                                }
                              ]
                            },
                            "condition": {
                              "arguments": [
                                {
                                  "arguments": [
                                    {
                                      "name": "dataEnd",
                                      "nodeType": "YulIdentifier",
                                      "src": "420:7:1"
                                    },
                                    {
                                      "name": "headStart",
                                      "nodeType": "YulIdentifier",
                                      "src": "429:9:1"
                                    }
                                  ],
                                  "functionName": {
                                    "name": "sub",
                                    "nodeType": "YulIdentifier",
                                    "src": "416:3:1"
                                  },
                                  "nodeType": "YulFunctionCall",
                                  "src": "416:23:1"
                                },
                                {
                                  "kind": "number",
                                  "nodeType": "YulLiteral",
                                  "src": "441:2:1",
                                  "type": "",
                                  "value": "64"
                                }
                              ],
                              "functionName": {
                                "name": "slt",
                                "nodeType": "YulIdentifier",
                                "src": "412:3:1"
                              },
                              "nodeType": "YulFunctionCall",
                              "src": "412:32:1"
                            },
                            "nodeType": "YulIf",
                            "src": "409:2:1"
                          },
                          {
                            "nodeType": "YulBlock",
                            "src": "471:128:1",
                            "statements": [
                              {
                                "nodeType": "YulVariableDeclaration",
                                "src": "486:15:1",
                                "value": {
                                  "kind": "number",
                                  "nodeType": "YulLiteral",
                                  "src": "500:1:1",
                                  "type": "",
                                  "value": "0"
                                },
                                "variables": [
                                  {
                                    "name": "offset",
                                    "nodeType": "YulTypedName",
                                    "src": "490:6:1",
                                    "type": ""
                                  }
                                ]
                              },
                              {
                                "nodeType": "YulAssignment",
                                "src": "515:74:1",
                                "value": {
                                  "arguments": [
                                    {
                                      "arguments": [
                                        {
                                          "name": "headStart",
                                          "nodeType": "YulIdentifier",
                                          "src": "561:9:1"
                                        },
                                        {
                                          "name": "offset",
                                          "nodeType": "YulIdentifier",
                                          "src": "572:6:1"
                                        }
                                      ],
                                      "functionName": {
                                        "name": "add",
                                        "nodeType": "YulIdentifier",
                                        "src": "557:3:1"
                                      },
                                      "nodeType": "YulFunctionCall",
                                      "src": "557:22:1"
                                    },
                                    {
                                      "name": "dataEnd",
                                      "nodeType": "YulIdentifier",
                                      "src": "581:7:1"
                                    }
                                  ],
                                  "functionName": {
                                    "name": "abi_decode_t_address_fromMemory",
                                    "nodeType": "YulIdentifier",
                                    "src": "525:31:1"
                                  },
                                  "nodeType": "YulFunctionCall",
                                  "src": "525:64:1"
                                },
                                "variableNames": [
                                  {
                                    "name": "value0",
                                    "nodeType": "YulIdentifier",
                                    "src": "515:6:1"
                                  }
                                ]
                              }
                            ]
                          },
                          {
                            "nodeType": "YulBlock",
                            "src": "609:129:1",
                            "statements": [
                              {
                                "nodeType": "YulVariableDeclaration",
                                "src": "624:16:1",
                                "value": {
                                  "kind": "number",
                                  "nodeType": "YulLiteral",
                                  "src": "638:2:1",
                                  "type": "",
                                  "value": "32"
                                },
                                "variables": [
                                  {
                                    "name": "offset",
                                    "nodeType": "YulTypedName",
                                    "src": "628:6:1",
                                    "type": ""
                                  }
                                ]
                              },
                              {
                                "nodeType": "YulAssignment",
                                "src": "654:74:1",
                                "value": {
                                  "arguments": [
                                    {
                                      "arguments": [
                                        {
                                          "name": "headStart",
                                          "nodeType": "YulIdentifier",
                                          "src": "700:9:1"
                                        },
                                        {
                                          "name": "offset",
                                          "nodeType": "YulIdentifier",
                                          "src": "711:6:1"
                                        }
                                      ],
                                      "functionName": {
                                        "name": "add",
                                        "nodeType": "YulIdentifier",
                                        "src": "696:3:1"
                                      },
                                      "nodeType": "YulFunctionCall",
                                      "src": "696:22:1"
                                    },
                                    {
                                      "name": "dataEnd",
                                      "nodeType": "YulIdentifier",
                                      "src": "720:7:1"
                                    }
                                  ],
                                  "functionName": {
                                    "name": "abi_decode_t_uint256_fromMemory",
                                    "nodeType": "YulIdentifier",
                                    "src": "664:31:1"
                                  },
                                  "nodeType": "YulFunctionCall",
                                  "src": "664:64:1"
                                },
                                "variableNames": [
                                  {
                                    "name": "value1",
                                    "nodeType": "YulIdentifier",
                                    "src": "654:6:1"
                                  }
                                ]
                              }
                            ]
                          }
                        ]
                      },
                      "name": "abi_decode_tuple_t_addresst_uint256_fromMemory",
                      "nodeType": "YulFunctionDefinition",
                      "parameters": [
                        {
                          "name": "headStart",
                          "nodeType": "YulTypedName",
                          "src": "361:9:1",
                          "type": ""
                        },
                        {
                          "name": "dataEnd",
                          "nodeType": "YulTypedName",
                          "src": "372:7:1",
                          "type": ""
                        }
                      ],
                      "returnVariables": [
                        {
                          "name": "value0",
                          "nodeType": "YulTypedName",
                          "src": "384:6:1",
                          "type": ""
                        },
                        {
                          "name": "value1",
                          "nodeType": "YulTypedName",
                          "src": "392:6:1",
                          "type": ""
                        }
                      ],
                      "src": "305:440:1"
                    },
                    {
                      "body": {
                        "nodeType": "YulBlock",
                        "src": "796:51:1",
                        "statements": [
                          {
                            "nodeType": "YulAssignment",
                            "src": "806:35:1",
                            "value": {
                              "arguments": [
                                {
                                  "name": "value",
                                  "nodeType": "YulIdentifier",
                                  "src": "835:5:1"
                                }
                              ],
                              "functionName": {
                                "name": "cleanup_t_uint160",
                                "nodeType": "YulIdentifier",
                                "src": "817:17:1"
                              },
                              "nodeType": "YulFunctionCall",
                              "src": "817:24:1"
                            },
                            "variableNames": [
                              {
                                "name": "cleaned",
                                "nodeType": "YulIdentifier",
                                "src": "806:7:1"
                              }
                            ]
                          }
                        ]
                      },
                      "name": "cleanup_t_address",
                      "nodeType": "YulFunctionDefinition",
                      "parameters": [
                        {
                          "name": "value",
                          "nodeType": "YulTypedName",
                          "src": "778:5:1",
                          "type": ""
                        }
                      ],
                      "returnVariables": [
                        {
                          "name": "cleaned",
                          "nodeType": "YulTypedName",
                          "src": "788:7:1",
                          "type": ""
                        }
                      ],
                      "src": "751:96:1"
                    },
                    {
                      "body": {
                        "nodeType": "YulBlock",
                        "src": "898:81:1",
                        "statements": [
                          {
                            "nodeType": "YulAssignment",
                            "src": "908:65:1",
                            "value": {
                              "arguments": [
                                {
                                  "name": "value",
                                  "nodeType": "YulIdentifier",
                                  "src": "923:5:1"
                                },
                                {
                                  "kind": "number",
                                  "nodeType": "YulLiteral",
                                  "src": "930:42:1",
                                  "type": "",
                                  "value": "0xffffffffffffffffffffffffffffffffffffffff"
                                }
                              ],
                              "functionName": {
                                "name": "and",
                                "nodeType": "YulIdentifier",
                                "src": "919:3:1"
                              },
                              "nodeType": "YulFunctionCall",
                              "src": "919:54:1"
                            },
                            "variableNames": [
                              {
                                "name": "cleaned",
                                "nodeType": "YulIdentifier",
                                "src": "908:7:1"
                              }
                            ]
                          }
                        ]
                      },
                      "name": "cleanup_t_uint160",
                      "nodeType": "YulFunctionDefinition",
                      "parameters": [
                        {
                          "name": "value",
                          "nodeType": "YulTypedName",
                          "src": "880:5:1",
                          "type": ""
                        }
                      ],
                      "returnVariables": [
                        {
                          "name": "cleaned",
                          "nodeType": "YulTypedName",
                          "src": "890:7:1",
                          "type": ""
                        }
                      ],
                      "src": "853:126:1"
                    },
                    {
                      "body": {
                        "nodeType": "YulBlock",
                        "src": "1030:32:1",
                        "statements": [
                          {
                            "nodeType": "YulAssignment",
                            "src": "1040:16:1",
                            "value": {
                              "name": "value",
                              "nodeType": "YulIdentifier",
                              "src": "1051:5:1"
                            },
                            "variableNames": [
                              {
                                "name": "cleaned",
                                "nodeType": "YulIdentifier",
                                "src": "1040:7:1"
                              }
                            ]
                          }
                        ]
                      },
                      "name": "cleanup_t_uint256",
                      "nodeType": "YulFunctionDefinition",
                      "parameters": [
                        {
                          "name": "value",
                          "nodeType": "YulTypedName",
                          "src": "1012:5:1",
                          "type": ""
                        }
                      ],
                      "returnVariables": [
                        {
                          "name": "cleaned",
                          "nodeType": "YulTypedName",
                          "src": "1022:7:1",
                          "type": ""
                        }
                      ],
                      "src": "985:77:1"
                    },
                    {
                      "body": {
                        "nodeType": "YulBlock",
                        "src": "1111:79:1",
                        "statements": [
                          {
                            "body": {
                              "nodeType": "YulBlock",
                              "src": "1168:16:1",
                              "statements": [
                                {
                                  "expression": {
                                    "arguments": [
                                      {
                                        "kind": "number",
                                        "nodeType": "YulLiteral",
                                        "src": "1177:1:1",
                                        "type": "",
                                        "value": "0"
                                      },
                                      {
                                        "kind": "number",
                                        "nodeType": "YulLiteral",
                                        "src": "1180:1:1",
                                        "type": "",
                                        "value": "0"
                                      }
                                    ],
                                    "functionName": {
                                      "name": "revert",
                                      "nodeType": "YulIdentifier",
                                      "src": "1170:6:1"
                                    },
                                    "nodeType": "YulFunctionCall",
                                    "src": "1170:12:1"
                                  },
                                  "nodeType": "YulExpressionStatement",
                                  "src": "1170:12:1"
                                }
                              ]
                            },
                            "condition": {
                              "arguments": [
                                {
                                  "arguments": [
                                    {
                                      "name": "value",
                                      "nodeType": "YulIdentifier",
                                      "src": "1134:5:1"
                                    },
                                    {
                                      "arguments": [
                                        {
                                          "name": "value",
                                          "nodeType": "YulIdentifier",
                                          "src": "1159:5:1"
                                        }
                                      ],
                                      "functionName": {
                                        "name": "cleanup_t_address",
                                        "nodeType": "YulIdentifier",
                                        "src": "1141:17:1"
                                      },
                                      "nodeType": "YulFunctionCall",
                                      "src": "1141:24:1"
                                    }
                                  ],
                                  "functionName": {
                                    "name": "eq",
                                    "nodeType": "YulIdentifier",
                                    "src": "1131:2:1"
                                  },
                                  "nodeType": "YulFunctionCall",
                                  "src": "1131:35:1"
                                }
                              ],
                              "functionName": {
                                "name": "iszero",
                                "nodeType": "YulIdentifier",
                                "src": "1124:6:1"
                              },
                              "nodeType": "YulFunctionCall",
                              "src": "1124:43:1"
                            },
                            "nodeType": "YulIf",
                            "src": "1121:2:1"
                          }
                        ]
                      },
                      "name": "validator_revert_t_address",
                      "nodeType": "YulFunctionDefinition",
                      "parameters": [
                        {
                          "name": "value",
                          "nodeType": "YulTypedName",
                          "src": "1104:5:1",
                          "type": ""
                        }
                      ],
                      "src": "1068:122:1"
                    },
                    {
                      "body": {
                        "nodeType": "YulBlock",
                        "src": "1239:79:1",
                        "statements": [
                          {
                            "body": {
                              "nodeType": "YulBlock",
                              "src": "1296:16:1",
                              "statements": [
                                {
                                  "expression": {
                                    "arguments": [
                                      {
                                        "kind": "number",
                                        "nodeType": "YulLiteral",
                                        "src": "1305:1:1",
                                        "type": "",
                                        "value": "0"
                                      },
                                      {
                                        "kind": "number",
                                        "nodeType": "YulLiteral",
                                        "src": "1308:1:1",
                                        "type": "",
                                        "value": "0"
                                      }
                                    ],
                                    "functionName": {
                                      "name": "revert",
                                      "nodeType": "YulIdentifier",
                                      "src": "1298:6:1"
                                    },
                                    "nodeType": "YulFunctionCall",
                                    "src": "1298:12:1"
                                  },
                                  "nodeType": "YulExpressionStatement",
                                  "src": "1298:12:1"
                                }
                              ]
                            },
                            "condition": {
                              "arguments": [
                                {
                                  "arguments": [
                                    {
                                      "name": "value",
                                      "nodeType": "YulIdentifier",
                                      "src": "1262:5:1"
                                    },
                                    {
                                      "arguments": [
                                        {
                                          "name": "value",
                                          "nodeType": "YulIdentifier",
                                          "src": "1287:5:1"
                                        }
                                      ],
                                      "functionName": {
                                        "name": "cleanup_t_uint256",
                                        "nodeType": "YulIdentifier",
                                        "src": "1269:17:1"
                                      },
                                      "nodeType": "YulFunctionCall",
                                      "src": "1269:24:1"
                                    }
                                  ],
                                  "functionName": {
                                    "name": "eq",
                                    "nodeType": "YulIdentifier",
                                    "src": "1259:2:1"
                                  },
                                  "nodeType": "YulFunctionCall",
                                  "src": "1259:35:1"
                                }
                              ],
                              "functionName": {
                                "name": "iszero",
                                "nodeType": "YulIdentifier",
                                "src": "1252:6:1"
                              },
                              "nodeType": "YulFunctionCall",
                              "src": "1252:43:1"
                            },
                            "nodeType": "YulIf",
                            "src": "1249:2:1"
                          }
                        ]
                      },
                      "name": "validator_revert_t_uint256",
                      "nodeType": "YulFunctionDefinition",
                      "parameters": [
                        {
                          "name": "value",
                          "nodeType": "YulTypedName",
                          "src": "1232:5:1",
                          "type": ""
                        }
                      ],
                      "src": "1196:122:1"
                    }
                  ]
                },
                "contents": "{\n\n    function abi_decode_t_address_fromMemory(offset, end) -> value {\n        value := mload(offset)\n        validator_revert_t_address(value)\n    }\n\n    function abi_decode_t_uint256_fromMemory(offset, end) -> value {\n        value := mload(offset)\n        validator_revert_t_uint256(value)\n    }\n\n    function abi_decode_tuple_t_addresst_uint256_fromMemory(headStart, dataEnd) -> value0, value1 {\n        if slt(sub(dataEnd, headStart), 64) { revert(0, 0) }\n\n        {\n\n            let offset := 0\n\n            value0 := abi_decode_t_address_fromMemory(add(headStart, offset), dataEnd)\n        }\n\n        {\n\n            let offset := 32\n\n            value1 := abi_decode_t_uint256_fromMemory(add(headStart, offset), dataEnd)\n        }\n\n    }\n\n    function cleanup_t_address(value) -> cleaned {\n        cleaned := cleanup_t_uint160(value)\n    }\n\n    function cleanup_t_uint160(value) -> cleaned {\n        cleaned := and(value, 0xffffffffffffffffffffffffffffffffffffffff)\n    }\n\n    function cleanup_t_uint256(value) -> cleaned {\n        cleaned := value\n    }\n\n    function validator_revert_t_address(value) {\n        if iszero(eq(value, cleanup_t_address(value))) { revert(0, 0) }\n    }\n\n    function validator_revert_t_uint256(value) {\n        if iszero(eq(value, cleanup_t_uint256(value))) { revert(0, 0) }\n    }\n\n}\n",
                "id": 1,
                "language": "Yul",
                "name": "#utility.yul"
              }
            ] }

        self.abi = [
          {
            "inputs": [
              {
                "internalType": "address",
                "name": "_winner",
                "type": "address"
              },
              {
                "internalType": "uint256",
                "name": "_money",
                "type": "uint256"
              }
            ],
            "stateMutability": "nonpayable",
            "type": "constructor"
          },
          {
            "inputs": [],
            "name": "money",
            "outputs": [
              {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
              }
            ],
            "stateMutability": "view",
            "type": "function"
          },
          {
            "inputs": [],
            "name": "owner",
            "outputs": [
              {
                "internalType": "address",
                "name": "",
                "type": "address"
              }
            ],
            "stateMutability": "view",
            "type": "function"
          },
          {
            "inputs": [],
            "name": "paying_check",
            "outputs": [
              {
                "internalType": "bool",
                "name": "",
                "type": "bool"
              }
            ],
            "stateMutability": "view",
            "type": "function"
          },
          {
            "inputs": [],
            "name": "problem",
            "outputs": [
              {
                "internalType": "string",
                "name": "",
                "type": "string"
              }
            ],
            "stateMutability": "view",
            "type": "function"
          },
          {
            "inputs": [
              {
                "internalType": "bool",
                "name": "_flag",
                "type": "bool"
              }
            ],
            "name": "vote",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function"
          },
          {
            "inputs": [],
            "name": "vote_sum",
            "outputs": [
              {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
              }
            ],
            "stateMutability": "view",
            "type": "function"
          },
          {
            "inputs": [],
            "name": "winner",
            "outputs": [
              {
                "internalType": "address",
                "name": "",
                "type": "address"
              }
            ],
            "stateMutability": "view",
            "type": "function"
          },
          {
            "inputs": [
              {
                "internalType": "uint256",
                "name": "judges",
                "type": "uint256"
              }
            ],
            "name": "withdraw",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function"
          }
        ]

    def deploy(self, problem):
        """
        @note : deploys the contract suggestion
        :param problem:
        :return: user_address of the deployed contract

        """
        # compile our solidity
        install_solc("0.8.0")
        compile_sol = compile_standard(
            {
                "language": "Solidity",
                "sources": {
                    "Suggestion.sol": {
                        "content": self.suggestion_file
                    }
                },
                "settings": {
                    "outputSelection": {
                        "*": {
                            "*": ['abi', 'metadata', 'evm.bytecode', 'evm.sourceMap']
                        }
                    }
                },

            },
            solc_version="0.8.0",
        )

        with open("compiled_code.json", "w") as file:
            json.dump(compile_sol, file, indent=2)

        # get bytecode
        self.bytecode = compile_sol["contracts"]["Suggestion.sol"]["Suggestion"]["evm"]["bytecode"]["object"]
        # get abi
        self.abi = compile_sol["contracts"]["Suggestion.sol"]["Suggestion"]["abi"]

        # Creating the contract
        Suggestion = self.w3.eth.contract(abi=self.abi, bytecode=self.bytecode)

        # Submit the transaction that deploys the contract

        transaction = Suggestion.constructor(problem).buildTransaction(
            {
                "chainId": self.chain_id,
                "gasPrice": self.w3.eth.gas_price,
                "from": self.user_address,
                "nonce": self.nonce,
            }
        )
        # Sign
        signed_txn = self.w3.eth.account.sign_transaction(transaction, private_key=self.pvt_key)
        print("Deploying the contract!")
        # send it
        tx_hash = self.w3.eth.send_raw_transaction(signed_txn.rawTransaction)
        # wait
        tx_reciept = self.w3.eth.wait_for_transaction_receipt(tx_hash)
        print(f'Contract deployed {tx_reciept.contractAddress}')

        return tx_reciept.contractAddress

    def problem(self , address):
      # Creating the contract
      Suggestion = self.w3.eth.contract(abi=self.abi, bytecode=self.bytecode)
      return Suggestion.functions.problem().call()

    def solution(self, contract_address, name, solution, cost):
        self.count += 1
        # Calling the transaction
        Suggestion = self.w3.eth.contract(address=contract_address, abi=self.abi)

        suggestion_given = Suggestion.functions.newsolution(name, solution, int(cost)).buildTransaction(
            {
                "chainId": self.chain_id,
                "gasPrice": self.w3.eth.gas_price,
                "from": self.user_address,
                "nonce": self.nonce + self.count,

            }
        )
        signed_txn = self.w3.eth.account.sign_transaction(
            suggestion_given, private_key=self.pvt_key
        )
        tx_hash = self.w3.eth.send_raw_transaction(
            signed_txn.rawTransaction
        )
        tx_receipt = self.w3.eth.wait_for_transaction_receipt(tx_hash)

        return Suggestion.functions.task(self.user_address).call()

    def user_vote(self, vote: bool, contract_address: str, vote_address: str):
        """

        @note - each contract_address  can vote only once.
        :param vote: bool - true : +1 or false : -1
        :param contract_address: contract_address of the deployed contract
        :param vote_address:
        :return: The contract contract_address of the voted suggestion
                 None if already voted

        """
        if not self.flag:
            self.count += 1
            Suggestion = self.w3.eth.contract(address=contract_address, abi=self.abi)
            user_vote_tx = Suggestion.functions.uservote(True, vote_address).buildTransaction(
                {
                    "chainId": self.chain_id,
                    "gasPrice": self.w3.eth.gas_price,
                    "from": self.user_address ,
                    "nonce": self.nonce + self.count,

                }
            )

            signed_txn = self.w3.eth.account.sign_transaction(
                user_vote_tx, private_key=self.pvt_key
            )
            tx_hash = self.w3.eth.send_raw_transaction(
                signed_txn.rawTransaction
            )
            tx_receipt = self.w3.eth.wait_for_transaction_receipt(tx_hash)
            self.flag = True
            return Suggestion.functions.task(self.user_address).call()

    def endsuggestion(self, contract_address: str):
        """
        @note - can only be used by the owner of the contract
                ends the poll.
        :param contract_address:
        :return: the winner of the suggestion poll
        """
        self.count += 1
        Suggestion = self.w3.eth.contract(address=contract_address, abi=self.abi)

        suggestion_endpoll = Suggestion.functions.endsuggestion().buildTransaction(
            {
                "chainId": self.chain_id,
                "gasPrice": self.w3.eth.gas_price,
                "from": self.user_address,
                "nonce": self.nonce + self.count,

            }
        )
        signed_txn = self.w3.eth.account.sign_transaction(
            suggestion_endpoll, private_key=self.pvt_key
        )
        tx_hash = self.w3.eth.send_raw_transaction(
            signed_txn.rawTransaction
        )
        tx_receipt = self.w3.eth.wait_for_transaction_receipt(tx_hash)

        return Suggestion.functions.winner2().call()


