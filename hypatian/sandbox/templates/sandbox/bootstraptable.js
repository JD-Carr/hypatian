https://kapeli.com/cheat_sheets/Axios.docset/Contents/Resources/Documents/index

<form method="POST" action="{{ url_for('edit_profile', username=user.username|lower) }}">

$(function () {
  var oTable = new TableInit();
  oTable.Init();
});

function TableInit() {
  var oTableInit = new Object();

  oTableInit.Init = function () {
    $('#table').bootstrapTable({
      url: httpRequestUrl + '/admin/queryUserList',
      method: 'POST',
      striped: true,
      cache: false,
      pagination: true,
      sortOrder: "asc",
      queryParamsType: '',
      dataType: 'json',
      paginationShowPageGo: true,
      showJumpto: true,
      pageNumber: 1,
      queryParams: queryParams,
      sidePagination: 'server',
      pageSize: 10,
      pageList: [10, 20, 30, 40],
      search: false,
      silent: true,
      showRefresh: false,
      showToggle: false,
      minimumCountColumns: 2,
      uniqueId: "id",
      columns: [{
        checkbox: true,
        visible: false
      }, {
        field: 'id',
        title: 'ID',
        align: 'center',
        formatter: function (value, row, index) {
          return index + 1;
        }
      }, {
        field: 'name_first',
        title: 'Firstname',
        align: 'center',
        width: '230px'
      }, {
        field: 'name_last',
        title: 'Lastname',
        align: 'center'
      }, {
        field: 'date_of_birth',
        title: '开Date of Birth',
        align: 'center'
      }],
      responseHandler: function (res) {
        console.log(res);
        if(res.code == "200"){
          var patientInfo = res.data.list;
          var NewData = [];
          if (patientInfo.length) {
            for (var i = 0; i < patientInfo.length; i++) {
              var dataNewObj = {
                "name_first": '',
                'name_last': '',
                "date_of_birth": '',
              };
              dataNewObj.name_first = patientInfo[i].name_first;
              dataNewObj.name_last = patientInfo[i].name_last;
              dataNewObj.date_of_birth = patientInfo[i].date_of_birth.replace(/-/g,'/');
              NewData.push(dataNewObj);
            }
            console.log(NewData)
          }
          var data = {
            total: res.data.total,
            rows: NewData
          };
          return data;
        }
      }
    });
  };

  function queryParams(params) {
    var nameLast = $("#keyWord").val();
    console.log(nameLast);
    var temp = {
      pageNum: params.pageNumber,
      pageSize: params.pageSize,
      name_last: nameLast
    };
    return JSON.stringify(temp);
  }

  return oTableInit;
}

function addFunctionAlty(value, row, index) {
  var btnText = '';

  btnText += "<button type=\"button\" id=\"btn_look\" οnclick=\"resetPassword(" + "'" + row.id + "'" + ")\" style='width: 77px;' class=\"btn btn-default-g ajax-link\">重置密码</button>&nbsp;&nbsp;";

  btnText += "<button type=\"button\" id=\"btn_look\" οnclick=\"openCreateUserPage(" + "'" + row.id + "'" + "," + "'编辑')\" class=\"btn btn-default-g ajax-link\">编辑</button>&nbsp;&nbsp;";

  btnText += "<button type=\"button\" id=\"btn_stop" + row.id + "\" οnclick=\"changeStatus(" + "'" + row.id + "'" + ")\" class=\"btn btn-danger-g ajax-link\">关闭</button>&nbsp;&nbsp;";

  btnText += "<button type=\"button\" id=\"btn_stop" + row.id + "\" οnclick=\"deleteUser(" + "'" + row.id + "'" + ")\" class=\"btn btn-danger-g ajax-link\">删除</button>&nbsp;&nbsp;";

  return btnText;
}

function getUserList() {
  $("#table").bootstrapTable('refresh');
}

$(function() {
  // test to ensure jQuery is working
  console.log("jQuery functional")

  // disable refresh button
  $("#refresh-btn").prop("disabled", true)
}
